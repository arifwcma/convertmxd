import arcpy
import os

print("Start")
aprx = arcpy.mp.ArcGISProject(r"C:\Files\mig\blank.aprx")
aprx.importDocument(r"C:\files\mig\Original\A0_landscapeA.mxd")
os.makedirs(r"C:\files\mig\Converted\A0_landscapeA", exist_ok=True)
aprx.saveACopy(r"C:\files\mig\Converted\A0_landscapeA\A0_landscapeA.aprx")
print("End")
