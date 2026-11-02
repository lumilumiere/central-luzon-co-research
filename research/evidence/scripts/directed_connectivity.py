"""Directed connectivity of the drivable OSM network in the corridor bounding box.
Builds a directed graph from way node sequences using oneway tags (yes/1/true forward, -1 reverse,
roundabout implies forward), then compares weakly and strongly connected components.
This is a topology diagnostic, not a SUMO build or a routing validation: turn restrictions,
access restrictions and bbox edge effects are not modelled.
Usage: python -I directed_connectivity.py <out_raw.json> <out_result.csv> [cached.json]"""
import csv,hashlib,json,sys,collections,requests
import networkx as nx
raw,out=sys.argv[1:3]
if len(sys.argv)>3: J=json.load(open(sys.argv[3],encoding='utf8')); ts=J['osm3s']['timestamp_osm_base']
else:
    Q='[out:json][timeout:110];way["highway"~"^(motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link|tertiary|tertiary_link|unclassified|residential|living_street|road)$"](15.16,120.24,15.43,120.64);out body;'
    for ep in ['https://overpass-api.de/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass.private.coffee/api/interpreter']:
        try:
            r=requests.post(ep,data={'data':Q},headers={'User-Agent':'geo-access-check/0.1'},timeout=130); print(ep,r.status_code)
            if r.status_code==200 and r.content[:1]==b'{': break
        except requests.RequestException as e: print(ep,type(e).__name__)
    else: sys.exit('all Overpass endpoints failed')
    open(raw,'wb').write(r.content); J=r.json(); ts=J['osm3s']['timestamp_osm_base']; print('sha256',hashlib.sha256(r.content).hexdigest())
G=nx.DiGraph(); ow=collections.Counter()
for w in J['elements']:
    t=w.get('tags',{}); n=w['nodes']; o=t.get('oneway','')
    if t.get('junction') in('roundabout','circular') and o=='': o='yes'
    if t.get('highway') in('motorway',) and o=='': o='yes'   # OSM convention: motorway implies oneway
    ow[o or 'none']+=1
    for a,b in zip(n,n[1:]):
        if o in('yes','1','true'): G.add_edge(a,b)
        elif o=='-1': G.add_edge(b,a)
        else: G.add_edge(a,b); G.add_edge(b,a)
w=list(nx.weakly_connected_components(G)); s=list(nx.strongly_connected_components(G))
N=G.number_of_nodes(); lw=max(len(c) for c in w); ls=max(len(c) for c in s)
big=max(s,key=len); E=G.number_of_edges(); Ein=sum(1 for a,b in G.edges if a in big and b in big)
rows=[('osm_snapshot',ts),('ways',len(J['elements'])),('nodes',N),('directed_edges',E),('oneway_tag_counts',dict(ow)),
      ('weak_components',len(w)),('largest_weak_share_of_nodes',round(lw/N,4)),('strong_components',len(s)),
      ('largest_strong_share_of_nodes',round(ls/N,4)),('edges_inside_largest_strong',round(Ein/E,4)),
      ('strong_components_size_ge_10',sum(1 for c in s if len(c)>=10))]
csv.writer(open(out,'w',newline='')).writerows([('metric','value')]+rows)
for r in rows: print(*r)
