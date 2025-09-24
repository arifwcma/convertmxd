import arcpy

print("Start")
src_mxd = r"I:\Admin\Software\ESRI\MapTemplates\WCMA Layouts\Additional_MXDs\Wetlands.mxd"
aprx = arcpy.mp.ArcGISProject(r"C:\users\m.rahman\arcgis\blank\blank.aprx")
aprx.importDocument(src_mxd)
aprx.saveACopy(fr"C:\users\m.rahman\arcgis\Wetlands\Wetlands.aprx")
print("End")
