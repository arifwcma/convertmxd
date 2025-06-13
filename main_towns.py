import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\Files\old\blank.aprx")
aprx.importDocument(r"C:\Files\old\20250520_VLP_Boundaries.mxd")
sde_path = r"C:\Files\old\MXDs\blank\PostgreSQL-gisap01-sdc(gisuser)2.sde"

def resolve_group(map_obj, path_parts):
    current = None
    for part in path_parts:
        candidates = map_obj.listLayers(current) if current else map_obj.listLayers()
        current = next((g for g in candidates if g.isGroupLayer and g.name == part), None)
        if current is None:
            return None
    return current

for m in aprx.listMaps():
    for lyr in m.listLayers():
        if lyr.name == "Main towns":
            try:
                path_parts = lyr.longName.split("\\")[:-1]
                group = resolve_group(m, path_parts)

                print(f"Found 'Main towns' under: {' > '.join(path_parts) if path_parts else '[Top Level]'}")

                new_lyr = arcpy.MakeQueryLayer_management(
                    input_database=sde_path,
                    out_layer_name="Main towns",
                    query="SELECT * FROM vicmap.lite_locality WHERE _wcma_int=true AND hierarchy<7",
                    oid_fields="ogc_fid",
                    shape_type="POINT",
                    srid=3111
                )[0]

                if group:
                    m.addLayerToGroup(group, new_lyr, "BOTTOM")
                    print("Inserted into group:", group.name)
                else:
                    m.addLayer(new_lyr)
                    print("Inserted at top level")

                m.removeLayer(lyr)
                print("Removed broken layer")

            except Exception as e:
                print("Fix failed:", e)

aprx.saveACopy(r"C:\Files\dest.aprx")
