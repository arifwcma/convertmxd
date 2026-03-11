import arcpy
import os
import shutil


dest = r"I:\Jobs\20252026\Arif\sandbox\aprx"
blank_folder = r"I:\Jobs\20252026\Arif\sandbox\assets\blank"
src_mxd = r"I:\Jobs\20252026\Arif\sandbox\mxd\18_WetlandsRamsar.mxd"
file_wo_mxd = "18_WetlandsRamsar"
d = os.path.join(dest, file_wo_mxd)
shutil.copytree(blank_folder, d, dirs_exist_ok=True)
blank_aprx = os.path.join(d, "blank.aprx")
final_aprx = os.path.join(d, file_wo_mxd + ".aprx")

print("Start",file_wo_mxd)
aprx = arcpy.mp.ArcGISProject(blank_aprx)
aprx.importDocument(src_mxd)
aprx.saveACopy(final_aprx)
print("End", file_wo_mxd)
