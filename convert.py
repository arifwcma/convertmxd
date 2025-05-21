import arcpy
import os

mxd_path = r"C:\Files\MXDs\20250520_VLP_Boundaries.mxd"
template_aprx = r"C:\Files\blank.aprx"
output_aprx = r"C:\Files\20250520_VLP_Boundaries.aprx"

aprx = arcpy.mp.ArcGISProject(template_aprx)
aprx.importDocument(mxd_path)
aprx.saveACopy(output_aprx)
