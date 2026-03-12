import arcpy
import os

sde_file = r"I:\Jobs\20252026\Arif\sandbox\assets\blank\db.sde"

print("=== Describe .sde file ===")
desc = arcpy.Describe(sde_file)
for prop in ['connectionString', 'connectionProperties', 'workspaceType', 'workspaceFactoryProgID', 'dataType', 'catalogPath']:
    try:
        val = getattr(desc, prop, 'N/A')
        print(f"  {prop}: {val}")
    except:
        print(f"  {prop}: (error)")

print("\n=== CIM from one broken SDE layer ===")
dest = r"I:\Jobs\20252026\Arif\sandbox\aprx"
d = os.path.join(dest, "18_WetlandsRamsar")
final_aprx = os.path.join(d, "18_WetlandsRamsar.aprx")

aprx = arcpy.mp.ArcGISProject(final_aprx)
for m in aprx.listMaps():
    for lyr in m.listLayers():
        if lyr.isBroken and lyr.supports("connectionProperties"):
            cp = lyr.connectionProperties
            if cp and cp.get('workspace_factory') == 'SDE':
                print(f"  Layer: {lyr.name}")
                try:
                    lyrCIM = lyr.getDefinition('V3')
                    dc = lyrCIM.featureTable.dataConnection
                    print(f"  CIM type: {type(dc).__name__}")
                    print(f"  workspaceConnectionString: {dc.workspaceConnectionString}")
                    print(f"  workspaceFactory: {dc.workspaceFactory}")
                    print(f"  dataset: {dc.dataset}")
                except Exception as e:
                    print(f"  Error: {e}")
                break
    break
