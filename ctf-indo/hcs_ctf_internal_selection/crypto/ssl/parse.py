from Crypto.Util.number import *

with open("my_private.pem", "r") as f:
    raw = f.read()

import base64

key_b64 = "".join(raw.split("\n")[1:-1])
key_bytes = base64.b64decode(
    key_b64.replace("_", "A")[:-2] + "=="
)
key_mask = base64.b64decode(
    "".join([
        "/" if i != "_" else "A"
        for i in key_b64
    ])[:-2] + "=="
)

print("Key length:", len(key_bytes))
print("Key hex   :", key_bytes.hex())
print("Key mask  :", key_mask.hex())

def der_unpack(bytes_stream):
    take_pos = 0
    def take(n_bytes, to_int=True):
        nonlocal take_pos
        res = bytes_stream[take_pos:take_pos + n_bytes]
        take_pos += n_bytes

        if to_int:
            res = int("0" + res.hex(), 16)
        return res, (take_pos - n_bytes, take_pos)

    tag, _ = take(1)
    length, _ = take(1)
    if length > 127:
        length, _ = take(length & 0x7f)

    print("Tag:", hex(tag), "Length:", length)

    res = None

    if tag == 0x30:
        res = []
        inner_data, _ = take(length, to_int=False)
        inner_pos = 0
        while inner_pos < length:
            inner_res, inner_used = der_unpack(inner_data[inner_pos:])
            res.append(inner_res)
            inner_pos += inner_used
    elif tag == 0x02:
        res, _ = take(length)

    return res, take_pos

unpacked_one, _ = der_unpack(key_bytes)
d = unpacked_one[3][3]
n = unpacked_one[3][1]
e = unpacked_one[3][2]
print(f"""
{d = }
{e = }
{n = }
""")

flag = bytes_to_long(open('flag.enc','rb').read())
print("Flag :",long_to_bytes(pow(flag,d,n)).decode('latin-1'))
