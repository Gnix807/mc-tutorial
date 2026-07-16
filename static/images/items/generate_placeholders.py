import os
import zlib
import struct

# 物品颜色字典 (RGB)
item_colors = {
    "oak_planks": (150, 110, 70),
    "spruce_planks": (100, 75, 45),
    "birch_planks": (195, 180, 130),
    "jungle_planks": (160, 115, 80),
    "acacia_planks": (170, 95, 55),
    "dark_oak_planks": (65, 43, 21),
    "mangrove_planks": (120, 50, 50),
    "cherry_planks": (220, 160, 160),
    "bamboo_planks": (180, 160, 80),
    "crimson_planks": (100, 40, 60),
    "warped_planks": (55, 110, 110),
    "stick": (200, 150, 80),
    "coal": (40, 40, 40),
    "charcoal": (50, 50, 50),
    "cobblestone": (128, 128, 128),
    "raw_iron": (210, 160, 110),
    "iron_ingot": (220, 220, 220),
    "wooden_pickaxe": (150, 110, 70),
    "stone_pickaxe": (128, 128, 128),
    "iron_pickaxe": (220, 220, 220),
    "wooden_shovel": (150, 110, 70),
    "stone_shovel": (128, 128, 128),
    "iron_shovel": (220, 220, 220),
    "wooden_axe": (150, 110, 70),
    "stone_axe": (128, 128, 128),
    "iron_axe": (220, 220, 220),
    "wooden_sword": (150, 110, 70),
    "stone_sword": (128, 128, 128),
    "iron_sword": (220, 220, 220),
    "wooden_hoe": (150, 110, 70),
    "stone_hoe": (128, 128, 128),
    "iron_hoe": (220, 220, 220),
    "furnace": (90, 90, 90),
    "crafting_table": (120, 90, 60),
    "chest": (160, 110, 50),
    "smooth_stone": (180, 180, 180),
    "raw_iron_block": (190, 140, 90),
    "iron_block": (235, 235, 235),
    "coal_block": (20, 20, 20),
    "lava_bucket": (230, 80, 10),
    "dried_kelp_block": (50, 70, 40),
    "blaze_rod": (240, 200, 20),
    "blast_furnace": (70, 70, 75),
    "smoker": (100, 80, 60)
}

dest_dir = os.path.dirname(os.path.abspath(__file__))

def make_png(width, height, color):
    # PNG signature
    png = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    png += struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', zlib.crc32(b'IHDR' + ihdr_data))
    
    # IDAT chunk
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00' # Filter type 0
        for x in range(width):
            raw_data += bytes(color)
            
    idat_data = zlib.compress(raw_data)
    png += struct.pack('>I', len(idat_data)) + b'IDAT' + idat_data + struct.pack('>I', zlib.crc32(b'IDAT' + idat_data))
    
    # IEND chunk
    png += struct.pack('>I', 0) + b'IEND' + struct.pack('>I', zlib.crc32(b'IEND'))
    return png

# 生成所有占位图
for key, color in item_colors.items():
    dest_file = os.path.join(dest_dir, f"{key}.png")
    # Only generate if file doesn't exist or is 0 bytes
    if not os.path.exists(dest_file) or os.path.getsize(dest_file) == 0:
        png_bytes = make_png(16, 16, color)
        with open(dest_file, "wb") as f:
            f.write(png_bytes)
        print(f"Generated placeholder {key}.png")
