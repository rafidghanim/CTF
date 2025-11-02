import base64
with open("demo_key.pem", "r") as f:
    demo_raw = f.read()

demo_b64 = "".join(demo_raw.split("\n")[1:-1])
demo_bytes = base64.b64decode(
    demo_b64.replace("_", "A")
)

unpacked_demo, _ = der_unpack(demo_bytes)
print(unpacked_demo)
