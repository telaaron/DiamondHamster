import csv, sys, os, json, gzip, re, time, urllib.request, statistics
from html.parser import HTMLParser
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
ev_path, docdir, usdir, out = sys.argv[1:5]
rows = list(csv.DictReader(open(ev_path)))
BLOCK = {'p','div','br','tr','li','h1','h2','h3','h4','h5','h6','table','ul','ol','section','article','header','footer','blockquote','pre','hr','dl','dt','dd','center','title','body','html','thead','tbody','tfoot','caption','form','address','page','document','type','sequence','filename','description','text'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.lines=[]; s.cur=[]; s.skip=0; s.cells=None; s.cell=None
    def flush(s):
        t=re.sub(r'[ \t\r\f\v\xa0​]+',' ',''.join(s.cur)).strip(); s.cur=[]
        if t: s.lines.append(t)
    def handle_starttag(s,tag,a):
        if tag in ('script','style'): s.skip+=1; return
        if s.skip: return
        if tag=='tr': s.flush(); s.cells=[]
        elif tag in ('td','th') and s.cells is not None:
            s.cell=[]
        elif tag in BLOCK:
            if s.cell is not None: s.cell.append(' ')
            else: s.flush()
    def handle_startendtag(s,tag,a):
        if tag in ('br','hr','p','div'):
            if s.cell is not None: s.cell.append(' ')
            else: s.flush()
    def handle_endtag(s,tag):
        if tag in ('script','style'): s.skip=max(0,s.skip-1); return
        if s.skip: return
        if tag in ('td','th') and s.cell is not None:
            c=re.sub(r'\s+',' ',''.join(s.cell).replace('\xa0',' ').replace('​','')).strip()
            s.cells.append(c); s.cell=None
        elif tag=='tr' and s.cells is not None:
            if s.cell is not None: s.handle_endtag('td')
            c=[x for x in s.cells if x]
            if c: s.lines.append(' | '.join(c))
            s.cells=None
        elif tag in BLOCK:
            if s.cell is not None: s.cell.append(' ')
            else: s.flush()
    def handle_data(s,d):
        if s.skip: return
        (s.cell if s.cell is not None else s.cur).append(d)
def totext(h):
    p=P(); p.feed(h); p.close()
    if p.cells is not None:
        if p.cell is not None: p.handle_endtag('td')
        p.handle_endtag('tr')
    p.flush(); return '\n'.join(p.lines)
# 1
missing=[]; nw=[]; ixh=0; n=0
with gzip.open(f'{out}/sec_8k_text.jsonl.gz','wt',encoding='utf-8') as g:
    for r in rows:
        fp=os.path.join(docdir,r['accession']+'.html')
        if not os.path.exists(fp): missing.append(r['accession']); continue
        raw=open(fp,'rb').read()
        h=raw.decode('utf-8',errors='replace') if b'\xef\xbf\xbd' not in raw[:0] else ''
        try: h=raw.decode('utf-8')
        except UnicodeDecodeError: h=raw.decode('latin-1')
        if 'ix:header' in h.lower(): ixh+=1
        t=totext(h); w=len(t.split()); nw.append(w); n+=1
        g.write(json.dumps({'accession':r['accession'],'ticker':r['ticker'],'n_words':w,'text':t},ensure_ascii=False)+'\n')
json.dump({'n':n,'missing':missing,'median':statistics.median(nw),'p300':sum(x>=300 for x in nw)/len(nw),
  'min':min(nw),'max':max(nw),'q25':statistics.quantiles(nw,n=4)[0],'q75':statistics.quantiles(nw,n=4)[2],'ix_header_docs':ixh},open(f'{out}/text_stats.json','w'),indent=1)
# 3
ET=ZoneInfo('America/New_York'); cache={}; cnt={'exact':0,'later':0,'none':0}
with open(f'{out}/a2s_entry.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['accession','ticker','entry_bar_et','bar_ts_utc','open','matched'])
    for r in rows:
        t=r['ticker']
        if t not in cache:
            fp=os.path.join(usdir,t+'.csv')
            cache[t]=[(int(x['ts']),x['open']) for x in csv.DictReader(open(fp))] if os.path.exists(fp) else []
        e=datetime.fromisoformat(r['entry_bar_et']); ems=int(e.timestamp()*1000); day=e.astimezone(ET).date()
        hit=None; m='none'
        for ts,o in sorted(cache[t]):
            if ts<ems: continue
            if datetime.fromtimestamp(ts/1000,timezone.utc).astimezone(ET).date()!=day: break
            if o in ('',None): continue
            hit=(ts,o); m='exact' if ts==ems else 'later'; break
        cnt[m]+=1
        w.writerow([r['accession'],t,r['entry_bar_et'],
          datetime.fromtimestamp(hit[0]/1000,timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') if hit else '', hit[1] if hit else '', m])
json.dump(cnt,open(f'{out}/entry_stats.json','w'))
# 2
UA='DiamondHamster research admin@must-seen.com'; errs=[]
ciks=sorted({int(r['cik']) for r in rows})
with open(f'{out}/sec_names.csv','w',newline='') as f, open(f'{out}/names_request.log','w') as lg:
    w=csv.writer(f); w.writerow(['cik','name','former_names'])
    for c in ciks:
        url=f'https://data.sec.gov/submissions/CIK{c:010d}.json'
        for att in range(4):
            t0=time.time()
            try:
                req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept-Encoding':'identity'})
                with urllib.request.urlopen(req,timeout=30) as resp: d=json.load(resp); st=resp.status
                lg.write(f'{datetime.now(timezone.utc).isoformat()} {st} {url}\n'); break
            except Exception as ex:
                lg.write(f'{datetime.now(timezone.utc).isoformat()} ERR {ex} {url}\n'); d=None; time.sleep(2**att)
            finally: time.sleep(max(0,0.15-(time.time()-t0)))
        if d is None: errs.append(c); w.writerow([c,'','']); continue
        w.writerow([c,d.get('name',''),';'.join(x.get('name','') for x in d.get('formerNames',[]) or [])])
json.dump({'n_ciks':len(ciks),'errors':errs},open(f'{out}/names_stats.json','w'))
