import arcpy

def traverse_layers(map_obj, parent=None, visited=None):
    if parent is None:
        print("Top level")
    else:
        print("Parent is: ", parent.longName)
    if visited is None:
        visited = set()

    children = []
    if parent is None:
        children = [lyr for lyr in map_obj.listLayers() if lyr.longName.count("\\") == 0]
    else:
        children = map_obj.listLayers(parent)

    print(len(children)," Children: ", [child.longName for child in children])

    for lyr in children:
        if lyr.longName in visited:
            continue
        visited.add(lyr.longName)
        print("Finished visiting ",lyr.longName)
        if lyr.isGroupLayer:
            traverse_layers(map_obj, parent=lyr, visited=visited)

def main():
    mxd_path = r"C:\Files\MXDs\IPAWS_Floodplain_.mxd"
    blank_aprx = r"C:\Files\old\blank.aprx"
    aprx = arcpy.mp.ArcGISProject(blank_aprx)
    aprx.importDocument(mxd_path)

    for m in aprx.listMaps():
        print(f"Map: {m.name}")
        traverse_layers(m)

    aprx.saveACopy(r"C:\Files\dest.aprx")

if __name__ == "__main__":
    main()
