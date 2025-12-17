import arcpy

print("Start")
src_mxd = r"C:\Users\m.rahman\mixed\jacqui\fig2\WCMA_region.mxd"
aprx = arcpy.mp.ArcGISProject(r"C:\users\m.rahman\arcgis\blank\blank.aprx")
aprx.importDocument(src_mxd)
aprx.saveACopy(fr"C:\Users\m.rahman\mixed\jacqui\fig2\fig2\aprx.aprx")
print("End")
