import arcpy
import os

mxd_folder = r"C:\Files\MXDs"
template_aprx = r"C:\Files\blank.aprx"
output_folder = r"C:\Files\Converted"

for file in os.listdir(mxd_folder):
    if file.lower().endswith(".mxd"):
        mxd_path = os.path.join(mxd_folder, file)
        new_aprx_path = os.path.join(output_folder, file.replace(".mxd", ".aprx"))
        aprx = arcpy.mp.ArcGISProject(template_aprx)
        aprx.importDocument(mxd_path)
        aprx.saveACopy(new_aprx_path)

