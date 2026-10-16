import sys, os, re, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *
import xml.etree.ElementTree as ET
BASE = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
NS = "{http://s3.amazonaws.com/doc/2006-03-01/}"
def s3list(prefix, delimiter="/"):
    keys, prefixes, marker = [], [], None
    while True:
        p = {"delimiter": delimiter, "prefix": prefix}
        if marker: p["marker"] = marker
        r = get(BASE, params=p)
        root = ET.fromstring(r.content)
        for c in root.findall(NS + "Contents"):
            keys.append(c.find(NS + "Key").text)
        for c in root.findall(NS + "CommonPrefixes"):
            prefixes.append(c.find(NS + "Prefix").text)
        if root.find(NS + "IsTruncated").text != "true":
            break
        nm = root.find(NS + "NextMarker")
        marker = nm.text if nm is not None else (keys[-1] if keys else prefixes[-1])
    return keys, prefixes
if __name__ == "__main__":
    res = {}
    for g in ("monthly", "daily"):
        _, pf = s3list(f"data/spot/{g}/klines/")
        res[g] = [p.split("/")[-2] for p in pf]
        print(g, len(res[g]))
    json.dump(res, open(os.path.join(os.path.dirname(__file__), "..", "symbols_all.json"), "w"))
