from PIL import Image
import os

def rgb_to_hex(rgb):
	return "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

result = ""
for i in range(0, 24):
	img = Image.open(f"frame_{i}.png")
	img = img.convert("RGB")
	pixel = img.getpixel((50, 50))
	h = rgb_to_hex(pixel)
	result += h
print(bytes.fromhex(result))
