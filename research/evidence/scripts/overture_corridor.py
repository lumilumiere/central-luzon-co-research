"""Overture places and buildings in the corridor via DuckDB S3 range reads. Usage: python -I overture_corridor.py <release> <aoi_cod.gpkg> <out_dir>"""
import sys; sys.stdout.reconfigure(encoding="utf8",errors="replace")
import sys,duckdb,geopandas as gpd,pandas as pd,shapely
rel,aoi,o=sys.argv[1:4]; a=gpd.read_file(aoi); c=duckdb.connect()
c.execute("INSTALL httpfs; LOAD httpfs; SET s3_region='us-west-2'; SET http_timeout=120000; SET enable_progress_bar=false")
bb="bbox.xmin>120.24 AND bbox.xmax<120.64 AND bbox.ymin>15.16 AND bbox.ymax<15.43"
p=f"s3://overturemaps-us-west-2/release/{rel}/theme=places/type=place/*"
print(c.execute(f"DESCRIBE SELECT * FROM read_parquet('{p}',hive_partitioning=1) LIMIT 1").df()[['column_name','column_type']].to_string()[:2200],flush=True)
d=c.execute(f"SELECT id, names.primary AS name, brand.names.primary AS brand, confidence, bbox.xmin AS x, bbox.ymin AS y, to_json(taxonomy) AS cat, to_json(sources) AS src FROM read_parquet('{p}',hive_partitioning=1) WHERE {bb}").df(); print(d.shape,flush=True); d.to_parquet(f'{o}/overture_places_corridor.parquet')
res=[]
for r in a.itertuples():
    q=d[shapely.contains_xy(r.geometry,d.x.values,d.y.values)]; res.append(dict(unit=r.adm3_name,release=rel,places=len(q),with_brand=int(q.brand.notna().sum()),conf_ge_0_5=int((q.confidence>=.5).sum()),conf_ge_0_8=int((q.confidence>=.8).sum()))); print(res[-1],flush=True)
pd.DataFrame(res).to_csv(f'{o}/overture_places_counts.csv',index=False)
print(d.brand.value_counts().head(25).to_dict())
b=f"s3://overturemaps-us-west-2/release/{rel}/theme=buildings/type=building/*"
x=c.execute(f"SELECT bbox.xmin AS x0,bbox.xmax AS x1,bbox.ymin AS y0,bbox.ymax AS y1, sources[1].dataset AS src, height, num_floors, subtype, class FROM read_parquet('{b}',hive_partitioning=1) WHERE {bb}").df(); print(x.shape,flush=True)
x['cx']=(x.x0+x.x1)/2; x['cy']=(x.y0+x.y1)/2; res=[]
for r in a.itertuples():
    q=x[shapely.contains_xy(r.geometry,x.cx.values,x.cy.values)]
    res.append(dict(unit=r.adm3_name,release=rel,buildings=len(q),by_source=q.src.value_counts().to_dict(),with_height=int(q.height.notna().sum()),with_floors=int(q.num_floors.notna().sum()),with_subtype=int(q.subtype.notna().sum()),with_class=int(q['class'].notna().sum()))); print(res[-1],flush=True)
pd.DataFrame(res).to_csv(f'{o}/overture_buildings_counts.csv',index=False)
