import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\Files\blank.aprx")
aprx.importDocument(r"C:\Files\20250520_VLP_Boundaries.mxd")
aprx.saveACopy(r"C:\Files\20250520_VLP_Boundaries.aprx")
