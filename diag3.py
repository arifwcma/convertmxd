import arcpy

sde_file = r"I:\Jobs\20252026\Arif\sandbox\assets\blank\db.sde"

print("=== List feature classes in .sde ===")
arcpy.env.workspace = sde_file
fcs = arcpy.ListFeatureClasses()
if fcs:
    print(f"  Found {len(fcs)} feature classes")
    print(f"  First 3: {fcs[:3]}")

    fc_path = f"{sde_file}\\{fcs[0]}"
    print(f"\n=== Make temp layer from: {fcs[0]} ===")
    arcpy.management.MakeFeatureLayer(fc_path, "temp_lyr")
    temp_lyr = arcpy.mp.LayerFile("temp_lyr") if False else None

    p = arcpy.mp.ArcGISProject("CURRENT") if False else None

    lyr_obj = arcpy.mp.LayerFile(fc_path) if False else None

    result = arcpy.management.MakeFeatureLayer(fc_path, "temp_lyr2")
    lyr = result.getOutput(0)
    desc = arcpy.Describe(lyr)
    print(f"  connectionString: [{desc.connectionString}]")

    print(f"\n=== Try Describe on fc_path directly ===")
    desc2 = arcpy.Describe(fc_path)
    print(f"  connectionString: [{desc2.connectionString}]")
    print(f"  catalogPath: {desc2.catalogPath}")
else:
    print("  No feature classes found -- check if .sde connection works")
