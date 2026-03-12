import olefile

sde_file = r"I:\Jobs\20252026\Arif\sandbox\assets\blank\db.sde"

ole = olefile.OleFileIO(sde_file)
print("=== OLE streams ===")
for stream in ole.listdir():
    name = "/".join(stream)
    size = ole.get_size(name)
    print(f"  {name} ({size} bytes)")

print("\n=== Stream contents ===")
for stream in ole.listdir():
    name = "/".join(stream)
    data = ole.openstream(name).read()
    for encoding in ['utf-8', 'utf-16-le', 'latin-1']:
        try:
            text = data.decode(encoding)
            printable = ''.join(c if c.isprintable() or c in '\n\r\t' else '.' for c in text)
            if any(kw in printable.upper() for kw in ['SERVER', 'DATABASE', 'PASSWORD', 'INSTANCE', 'GISAP']):
                print(f"\n--- {name} ({encoding}) ---")
                print(printable[:2000])
                break
        except:
            continue

ole.close()
