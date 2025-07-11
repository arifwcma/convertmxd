import arcpy
import os

to_migrate = "A0_landscapeB"
print("Start")
aprx = arcpy.mp.ArcGISProject(r"C:\Files\mig\blank.aprx")
aprx.importDocument(fr"C:\files\mig\Original\{to_migrate}.mxd")
os.makedirs(fr"C:\files\mig\Converted\{to_migrate}", exist_ok=True)
aprx.saveACopy(fr"C:\files\mig\Converted\{to_migrate}\{to_migrate}.aprx")
print("End")
