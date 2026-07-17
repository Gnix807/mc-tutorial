from PIL import Image
import os

directory = 'static/images/items/'
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        filepath = os.path.join(directory, filename)
        img = Image.open(filepath).convert("RGBA")
        
        # Upscale by 16x using Nearest Neighbor
        new_size = (img.width * 16, img.height * 16)
        upscaled = img.resize(new_size, Image.Resampling.NEAREST)
        upscaled.save(filepath)
        print(f"Upscaled {filename} to {new_size}")
