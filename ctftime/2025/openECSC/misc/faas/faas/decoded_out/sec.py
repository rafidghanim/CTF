# make_pyc.py
import importlib.util, struct, time
marshalled = open("raw_decompressed.bin","rb").read()
magic = importlib.util.MAGIC_NUMBER
mtime = int(time.time())
# header: magic + 8 bytes (timestamp + size/hash) — ok for most decompilers
header = magic + struct.pack("<II", mtime, 0)
with open("maybe.pyc","wb") as f:
    f.write(header)
    f.write(marshalled)
print("Wrote maybe.pyc")
