import arcpy
import os
import shutil

src = r"I:\Programs\RDP Emergency Preparedness and Response Project\Maps"
dest = r"I:\Admin\Software\ESRI\MapTemplates\WCMA Layouts\ArcGISPro_Templates\Finalised\RDP_EPRP"
blank_folder = r"I:\Admin\Assets\blank"

for file in os.listdir(src):
    if file.endswith(".mxd"):
        src_mxd = os.path.join(src, file)
        file_wo_mxd = os.path.splitext(file)[0]
        d = os.path.join(dest, file)
        shutil.copytree(blank_folder, d, dirs_exist_ok=True)
        blank_aprx = os.path.join(d, "blank.aprx")
        final_aprx = os.path.join(d, file_wo_mxd + ".aprx")

        print("Start",file)
        aprx = arcpy.mp.ArcGISProject(blank_aprx)
        aprx.importDocument(src_mxd)
        aprx.saveACopy(final_aprx)
        print("End", file)
