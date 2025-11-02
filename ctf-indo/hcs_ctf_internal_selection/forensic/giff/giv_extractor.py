from PIL import Image
import os

def extract_frames(gif_path, output_folder):
    gif = Image.open(gif_path)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_number = 0
    while True:
        frame_path = os.path.join(output_folder, f"frame_{frame_number}.png")
        gif.save(frame_path, 'PNG')
        
        frame_number += 1
        try:
            gif.seek(gif.tell() + 1)
        except EOFError:
            break
    
    print(f"Extracted {frame_number} frames to {output_folder}")

gif_path = 'input.gif' 
output_folder = 'output_frames'
extract_frames(gif_path, output_folder)
