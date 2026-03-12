import arcpy
import os
import shutil

sde_file = r"I:\Jobs\20252026\Arif\sandbox\assets\blank\db.sde"

print("=== .sde connectionProperties object ===")
desc = arcpy.Describe(sde_file)
cp = desc.connectionProperties
for prop in ['server', 'instance', 'database', 'authentication_mode', 'user', 'password', 'version', 'historical_name', 'historical_timestamp']:
    try:
        val = getattr(cp, prop, 'N/A')
        print(f"  {prop}: {val}")
    except:
        print(f"  {prop}: (error)")

print("\n=== Fresh import for CIM inspection ===")
dest = r"I:\Jobs\20252026\Arif\sandbox\aprx"
blank_folder = r"I:\Jobs\20252026\Arif\sandbox\assets\blank"
src_mxd = r"I:\Jobs\20252026\Arif\sandbox\mxd\18_WetlandsRamsar.mxd"
file_wo_mxd = "18_WetlandsRamsar"
d = os.path.join(dest, file_wo_mxd)
shutil.copytree(blank_folder, d, dirs_exist_ok=True)
blank_aprx = os.path.join(d, "blank.aprx")
final_aprx = os.path.join(d, file_wo_mxd + ".aprx")

aprx = arcpy.mp.ArcGISProject(blank_aprx)
aprx.importDocument(src_mxd)

for m in aprx.listMaps():
    for lyr in m.listLayers():
        if lyr.isBroken and lyr.supports("connectionProperties"):
            cp2 = lyr.connectionProperties
            if cp2 and cp2.get('workspace_factory') == 'SDE':
                print(f"  Layer: {lyr.name}")
                try:
                    lyrCIM = lyr.getDefinition('V3')
                    dc = lyrCIM.featureTable.dataConnection
                    print(f"  CIM type: {type(dc).__name__}")
                    print(f"  workspaceConnectionString: [{dc.workspaceConnectionString}]")
                    print(f"  workspaceFactory: {dc.workspaceFactory}")
                    print(f"  dataset: {dc.dataset}")
                    if hasattr(dc, 'datasetType'):
                        print(f"  datasetType: {dc.datasetType}")
                except Exception as e:
                    print(f"  Error: {e}")
                break
    break

aprx.saveACopy(final_aprx)
print("Done")
