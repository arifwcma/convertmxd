import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\Files\old\blank.aprx")
aprx.importDocument(r"C:\Files\old\20250520_VLP_Boundaries.mxd")
sde_path = r"C:\Files\old\MXDs\blank\PostgreSQL-gisap01-sdc(gisuser)2.sde"

for m in aprx.listMaps():
    for lyr in m.listLayers():
        if lyr.name == "Main towns":
            try:
                new_lyr = arcpy.MakeQueryLayer_management(
                    input_database=sde_path,
                    out_layer_name="Main towns",
                    query="SELECT * FROM vicmap.lite_locality WHERE _wcma_int=true AND hierarchy<7",
                    oid_fields="ogc_fid",
                    shape_type="POINT",
                    srid=3111
                )[0]

                parent_group = None
                for group in m.listLayers():
                    if group.isGroupLayer:
                        if lyr.name in [child.name for child in m.listLayers(group)]:
                            parent_group = group
                            break

                if parent_group:
                    m.addLayerToGroup(parent_group, new_lyr, "BOTTOM")
                else:
                    m.addLayer(new_lyr)

                m.removeLayer(lyr)
                print("Main towns fixed")

            except Exception as e:
                print(f"Failed to fix Main towns: {e}")

aprx.saveACopy(r"C:\Files\dest.aprx")
