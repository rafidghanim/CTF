from PIL import Image
import os

def rgb_to_hex(rgb):
    """Convert an RGB tuple to a hex string."""
    return "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def extract_rgb_from_image(image_path):
    """Extract the RGB value from the center pixel of the image."""
    img = Image.open(image_path)
    img_rgb = img.convert('RGB')
    center_pixel = img_rgb.getpixel((img.size[0] // 2, img.size[1] // 2))
    return center_pixel

def solve(image_folder, frame_count):
    result = ""
    for i in range(frame_count):
        image_path = os.path.join(image_folder, f"frame_{i}.png")
        rgb = extract_rgb_from_image(image_path)
        hex_value = rgb_to_hex(rgb)
        result += hex_value

    return bytes.fromhex(result)

# Example usage:
image_folder = 'output_frames'  # Path to folder containing frames
frame_count = 25  # Total number of frames

# Call the solver function
final_output = solve(image_folder, frame_count)
print(final_output)
