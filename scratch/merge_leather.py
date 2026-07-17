from PIL import Image
import os

img_dir = r"c:\Users\Gnix807\Desktop\新建文件夹\MC教程\static\images\items"
pieces = ["leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots"]

for piece in pieces:
    base_path = os.path.join(img_dir, f"{piece}.png")
    overlay_path = os.path.join(img_dir, f"{piece}_overlay.png")
    out_path = os.path.join(img_dir, f"{piece}_default.png")
    
    if os.path.exists(base_path) and os.path.exists(overlay_path):
        base_img = Image.open(base_path).convert("RGBA")
        overlay_img = Image.open(overlay_path).convert("RGBA")
        
        # Composite overlay on top of base
        # base_img is the default brown leather color in the vanilla jar.
        combined = Image.alpha_composite(base_img, overlay_img)
        
        combined.save(out_path)
        print(f"Created {piece}_default.png")
    else:
        print(f"Missing base or overlay for {piece}")
