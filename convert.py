import arcpy

print("Hi")

aprx = arcpy.mp.ArcGISProject(r"C:\Files\old\blank.aprx")
aprx.importDocument(r"C:\Files\old\20250520_VLP_Boundaries.mxd")
sde_path = r"C:\Files\old\MXDs\blank\PostgreSQL-gisap01-sdc(gisuser)2.sde"

geometry_type_map = {
    "Point": "POINT",
    "Polyline": "LINE",
    "Polygon": "POLYGON"
}

candidate_shapes = ["geom", "shape", "the_geom"]
fallback_oid = "objectid"
default_srid = 7844
default_shape_type = "POLYGON"

for m in aprx.listMaps():
    for lyr in m.listLayers():

        if "Main towns" in lyr.name:
            print(lyr.name)
            print(lyr.isBroken)
            print(type(lyr))
            print(lyr.supports("connectionProperties"))
            print(lyr.connectionProperties)
        print("-----------------------")

        if lyr.isBroken and lyr.isFeatureLayer:
            query = lyr.connectionProperties.get("query")
            if not query:
                print(f"{lyr.name} skipped: no query found")
                continue
            try:
                shape_field = next((f for f in candidate_shapes if f.lower() in query.lower()), None)
                if not shape_field:
                    print(f"{lyr.name} skipped: no shape field detected in query")
                    continue
                shape_type = default_shape_type
                srid = default_srid
                print(f"{lyr.name} → shape_field: {shape_field}, oid_field: {fallback_oid}, shape_type: {shape_type}, srid: {srid}")
                new_lyr = arcpy.management.MakeQueryLayer(
                    input_database=sde_path,
                    out_layer_name=lyr.name,
                    query=query,
                    oid_fields=fallback_oid,
                    shape_type=shape_type,
                    srid=srid,
                    shape_field_name=shape_field
                )[0]
                m.removeLayer(lyr)
                m.addLayer(new_lyr)
            except Exception as e:
                print(f"{lyr.name} failed: {e}")

aprx.saveACopy(r"C:\Files\20250520_VLP_Boundaries_updated.aprx")
