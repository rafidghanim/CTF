import base64
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
with open("my_private.pem", "r") as f:
    demo_raw = f.read()

demo_b64 = "".join(demo_raw.split("\n")[1:-1])
demo_bytes = base64.b64decode(
    demo_b64.replace("x", "A")
)

unpacked_demo, _ = der_unpack(demo_bytes)
