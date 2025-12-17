import arcpy

print("Start")
src_mxd = r"C:\Users\m.rahman\mixed\savio\sites\MXDs\Sites_Master.mxd"
aprx = arcpy.mp.ArcGISProject(r"C:\Users\m.rahman\mixed\savio\sites\blank\blank.aprx")
aprx.importDocument(src_mxd)
aprx.saveACopy(fr"I:\Programs\RCS\2020\Maps\APRX_Wetlands\APRX_Wetlands.aprx")
print("End")
