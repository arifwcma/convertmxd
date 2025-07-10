import arcpy

print("Hi")

aprx = arcpy.mp.ArcGISProject(r"C:\Files\mig\blank.aprx")
aprx.importDocument(r"C:\Files\old\Bryana\IPAWS_A5.mxd")
#sde_path = r"C:\Files\old\MXDs\blank\PostgreSQL-gisap01-sdc(gisuser)2.sde"
dest = r"C:\Files\mig\dest2.aprx"
aprx.saveACopy(dest)

