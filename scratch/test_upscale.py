from PIL import Image, ImageFilter
import os

files = ['static/images/items/oak_planks.png', 'static/images/items/furnace.png', 'static/images/items/crafting_table.png']

for f in files:
    if os.path.exists(f):
        img = Image.open(f).convert("RGBA")
        if img.size == (32, 32):
            # Upscale 4x with Lanczos for smoothness
            upscaled = img.resize((128, 128), Image.Resampling.LANCZOS)
            
            # Apply Unsharp Mask to sharpen the smoothed edges
            sharpened = upscaled.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
            
            sharpened.save(f.replace('.png', '_upscaled.png'))
            print(f"Upscaled {f}")
