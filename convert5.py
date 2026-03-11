import arcpy
import os
import pprint
import shutil


dest = r"I:\Jobs\20252026\Arif\sandbox\aprx"
blank_folder = r"I:\Jobs\20252026\Arif\sandbox\assets\blank"
src_mxd = r"I:\Jobs\20252026\Arif\sandbox\mxd\18_WetlandsRamsar.mxd"
file_wo_mxd = "18_WetlandsRamsar"
d = os.path.join(dest, file_wo_mxd)
shutil.copytree(blank_folder, d, dirs_exist_ok=True)
blank_aprx = os.path.join(d, "blank.aprx")
final_aprx = os.path.join(d, file_wo_mxd + ".aprx")
sde_file = os.path.join(d, "db.sde")

print("Start", file_wo_mxd)
aprx = arcpy.mp.ArcGISProject(blank_aprx)
aprx.importDocument(src_mxd)

for m in aprx.listMaps():
    for lyr in m.listLayers():
        if lyr.isBroken:
            print(f"BROKEN: {lyr.name}")
            if lyr.supports("connectionProperties"):
                pprint.pprint(lyr.connectionProperties)
            else:
                print("  (connectionProperties not supported)")

for m in aprx.listMaps():
    for lyr in m.listLayers():
        if lyr.isBroken and lyr.supports("connectionProperties"):
            cp = lyr.connectionProperties
            if cp is not None and cp.get('workspace_factory') == 'SDE':
                print(f"  Fixing (Approach A): {lyr.name}")
                lyr.updateConnectionProperties(cp, sde_file, validate=False)

aprx.saveACopy(final_aprx)
print("End", file_wo_mxd)
