import arcpy

print("Start")
src_mxd = r"C:\Users\m.rahman\arcmap\Community_RAP_all_A6.mxd"
aprx = arcpy.mp.ArcGISProject(r"C:\Users\m.rahman\arcgis\rcs_fig1\rcs_fig1.aprx")
aprx.importDocument(src_mxd)
aprx.saveACopy(fr"C:\Users\m.rahman\arcgis\rcs_fig1\rcs_fig1_complete.aprx")
print("End")
