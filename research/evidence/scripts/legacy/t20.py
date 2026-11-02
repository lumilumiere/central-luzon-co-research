import sys,time,sqlite3
import geopandas as gpd
d=sys.argv[1]; a=gpd.read_file(f'{d}/aoi_cod.gpkg'); au=a.to_crs(32651)
f=f'{d}/mapillary.gpkg'
c=sqlite3.connect(f); print([r[0] for r in c.execute("select name from sqlite_master where type='table'")][:12]); print(c.execute('select * from gpkg_contents').fetchall()); 
t=time.time(); m=gpd.read_file(f,bbox=tuple(a.total_bounds),engine='pyogrio'); print(m.shape,round(time.time()-t),m.crs,flush=True)
print(m.drop(columns='geometry').iloc[0].to_string()[:1500])
m=m.to_crs(32651)
for r in au.itertuples():
    q=m.clip(r.geometry); q=q.assign(L=q.length/1000); print('\n',r.adm3_name,'rows',len(q),'km',round(q.L.sum(),1))
    for col in ['combined_surface_DL_priority','combined_surface_osm_priority','pred_label','osm_surface_class','urban']:
        if col in q: print('  ',col,q.groupby(col,dropna=False).L.sum().round(1).to_dict())
    p=q.predicted_length.fillna(0).sum()/1000; print('   predicted_length km',round(p,1),'DL ts',q.DL_mean_timestamp.dropna().min(),q.DL_mean_timestamp.dropna().max(),'osm ts max',q.osm_changeset_timestamp.dropna().max(),'n_pred median',q.n_of_predictions_used.dropna().median())
