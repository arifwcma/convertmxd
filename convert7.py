import arcpy
import os
import shutil


dest = r"I:\Jobs\20252026\Arif\sandbox\aprx"
blank_folder = r"I:\Jobs\20252026\Arif\sandbox\assets\blank"
src_mxd = r"I:\Jobs\20252026\Arif\sandbox\mxd\18_WetlandsRamsar.mxd"
file_wo_mxd = "18_WetlandsRamsar"
d = os.path.join(dest, file_wo_mxd)
shutil.copytree(blank_folder, d, dirs_exist_ok=True)
blank_aprx = os.path.join(d, "blank.aprx")
final_aprx = os.path.join(d, file_wo_mxd + ".aprx")

conn_string = (
    "SERVER=gisap01;"
    "INSTANCE=sde:postgresql:gisap01;"
    "DBCLIENT=postgresql;"
    "DB_CONNECTION_PROPERTIES=gisap01;"
    "DATABASE=sdc;"
    "USER=gisadmin;"
    "PASSWORD=geospatial;"
    "AUTHENTICATION_MODE=DBMS"
)

print("Start", file_wo_mxd)
aprx = arcpy.mp.ArcGISProject(blank_aprx)
aprx.importDocument(src_mxd)

fixed = 0
for m in aprx.listMaps():
    for lyr in m.listLayers():
        if lyr.isBroken:
            try:
                lyrCIM = lyr.getDefinition('V3')
                dc = lyrCIM.featureTable.dataConnection
                if hasattr(dc, 'workspaceFactory') and dc.workspaceFactory == 'SDE':
                    dc.workspaceConnectionString = conn_string
                    lyr.setDefinition(lyrCIM)
                    fixed += 1
                    print(f"  Fixed: {lyr.name}")
            except:
                pass

print(f"Fixed {fixed} SDE layers")
aprx.saveACopy(final_aprx)
print("End", file_wo_mxd)
