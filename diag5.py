import olefile
import sys
sys.stdout.reconfigure(encoding='utf-8')

sde_file = r"I:\Jobs\20252026\Arif\sandbox\assets\blank\db.sde"

ole = olefile.OleFileIO(sde_file)
data = ole.openstream("SDEConnProperties").read()
ole.close()

text = data.decode('utf-16-le', errors='replace')

for char in text:
    if char.isprintable() or char in '\r\n\t':
        sys.stdout.write(char)
    elif ord(char) > 0:
        sys.stdout.write(f'[{ord(char):04x}]')
sys.stdout.write('\n')

print("\n=== Key-value pairs ===")
import re
pairs = re.findall(r'([A-Z_]+)\s*=\s*([^\r\n;]+)', text)
for k, v in pairs:
    clean_v = ''.join(c if c.isprintable() else '' for c in v)
    print(f"  {k} = {clean_v}")
