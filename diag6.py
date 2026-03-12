import olefile
import sys
sys.stdout.reconfigure(encoding='utf-8')

sde_file = r"I:\Jobs\20252026\Arif\sandbox\assets\blank\db.sde"

ole = olefile.OleFileIO(sde_file)
data = ole.openstream("SDEConnProperties").read()
ole.close()

print(f"Raw hex ({len(data)} bytes):")
for i in range(0, len(data), 32):
    hex_part = data[i:i+32].hex()
    ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in data[i:i+32])
    print(f"  {i:04d}: {hex_part}  {ascii_part}")
