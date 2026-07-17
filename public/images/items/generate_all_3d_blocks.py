import os
import zipfile
import io
from PIL import Image

# 3D立方体在512x512画布下的绝对完美 30度等轴测仿射变换矩阵
# 保证长宽比例绝对不畸形，且方块大小完美撑满 512 画布边缘，使视觉体量等同于二维物品
top_matrix = (0.040163, 0.069565, -12.090550, -0.040163, 0.069565, 8.473159)
left_matrix = (0.080327, 0.0, -4.563710, -0.040163, 0.069565, -7.526840)
right_matrix = (0.080327, 0.0, -20.563710, 0.040163, 0.069565, -28.090550)

TOP_BRIGHTNESS = 1.0
LEFT_BRIGHTNESS = 0.8
RIGHT_BRIGHTNESS = 0.6

target_version_path = r"E:\BaiduNetdiskDownload\Earth3 ver0.21fix\.minecraft\versions\26.2"
dest_dir = "static/images/items"

def find_jar_in_folder(folder_path):
    if not os.path.exists(folder_path):
        return None
    for file in os.listdir(folder_path):
        if file.endswith(".jar"):
            jar_path = os.path.join(folder_path, file)
            if os.path.getsize(jar_path) > 5 * 1024 * 1024:
                return jar_path
    return None

def apply_brightness(im, factor):
    if factor == 1.0: return im
    r, g, b, a = im.split()
    r = r.point(lambda p: min(255, int(p * factor)))
    g = g.point(lambda p: min(255, int(p * factor)))
    b = b.point(lambda p: min(255, int(p * factor)))
    return Image.merge("RGBA", (r, g, b, a))

# 排除非实体方块的关键字
exclude_keywords = [
    "door", "trapdoor", "rail", "sapling", "flower", "coral", "plant", "crop", 
    "vine", "glass_pane", "torch", "lantern", "campfire", "bed", "cake", 
    "chain", "web", "wheat", "potato", "carrot", "beetroot", "stem", "mushroom", 
    "bars", "tripwire", "redstone_dust", "repeater", "comparator", "scaffolding",
    "bamboo", "kelp", "seagrass", "sugar_cane", "tall_grass", "fern", "lily_pad",
    "spawner", "command_block", "structure", "jigsaw", "barrier", "light", 
    "azalea", "dripleaf", "spore_blossom", "roots", "fire", "water", "lava", "portal",
    "_top", "_bottom", "_side", "_front", "_back", "_inner", "_outer"
]

def is_solid_block(name):
    for kw in exclude_keywords:
        if kw in name:
            return False
    return True

jar_path = find_jar_in_folder(target_version_path)

if jar_path:
    print("Scanning JAR for all solid blocks to convert to 3D...")
    rendered_count = 0
    with zipfile.ZipFile(jar_path, 'r') as jar:
        # 获取所有 block png
        block_files = [f for f in jar.namelist() if f.startswith("assets/minecraft/textures/block/") and f.endswith(".png") and f.count("/") == 4]
        block_names = [os.path.basename(f)[:-4] for f in block_files]
        
        for file in block_files:
            base_name = os.path.basename(file)
            block_name = base_name[:-4]
            
            if not is_solid_block(block_name):
                continue
                
            dest_file = os.path.join(dest_dir, base_name)
            
            # 智能匹配侧面和顶部
            top_name = f"{block_name}_top"
            side_name = f"{block_name}_side"
            front_name = f"{block_name}_front"
            
            top_tex = file
            left_tex = file
            right_tex = file
            
            # 尝试在库中寻找 _top
            if top_name in block_names:
                top_tex = f"assets/minecraft/textures/block/{top_name}.png"
            # 尝试寻找 _side
            if side_name in block_names:
                left_tex = f"assets/minecraft/textures/block/{side_name}.png"
                right_tex = f"assets/minecraft/textures/block/{side_name}.png"
            elif front_name in block_names:
                left_tex = f"assets/minecraft/textures/block/{front_name}.png"

            try:
                top_data = jar.read(top_tex)
                left_data = jar.read(left_tex)
                right_data = jar.read(right_tex)
            except KeyError:
                continue # 找不到则跳过
                
            try:
                top_im = Image.open(io.BytesIO(top_data)).convert("RGBA")
                left_im = Image.open(io.BytesIO(left_data)).convert("RGBA")
                right_im = Image.open(io.BytesIO(right_data)).convert("RGBA")
                
                # 剔除透明像素过多的方块 (超过 50% 像素完全透明，比如树叶的透明模式、玻璃)
                # 稍等，玻璃和树叶我们要保留 3D！所以不严格剔除透明。
                
                top_im = top_im.resize((16, 16), Image.Resampling.NEAREST)
                left_im = left_im.resize((16, 16), Image.Resampling.NEAREST)
                right_im = right_im.resize((16, 16), Image.Resampling.NEAREST)

                top_im = apply_brightness(top_im, TOP_BRIGHTNESS)
                left_im = apply_brightness(left_im, LEFT_BRIGHTNESS)
                right_im = apply_brightness(right_im, RIGHT_BRIGHTNESS)

                canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))

                transformed_top = top_im.transform((512, 512), Image.Transform.AFFINE, top_matrix, Image.Resampling.NEAREST)
                transformed_left = left_im.transform((512, 512), Image.Transform.AFFINE, left_matrix, Image.Resampling.NEAREST)
                transformed_right = right_im.transform((512, 512), Image.Transform.AFFINE, right_matrix, Image.Resampling.NEAREST)

                canvas = Image.alpha_composite(canvas, transformed_top)
                canvas = Image.alpha_composite(canvas, transformed_left)
                canvas = Image.alpha_composite(canvas, transformed_right)

                canvas.save(dest_file, "PNG")
                rendered_count += 1
                if rendered_count % 50 == 0:
                    print(f"Rendered {rendered_count} 3D blocks...")
            except Exception as e:
                print(f"Error rendering {block_name}: {e}")

        # 手动生成复合面的特殊方块 (功能性方块)
        compound_blocks = {
            "furnace": {"top": "furnace_top", "left": "furnace_front", "right": "furnace_side"},
            "crafting_table": {"top": "crafting_table_top", "left": "crafting_table_front", "right": "crafting_table_side"},
            "smithing_table": {"top": "smithing_table_top", "left": "smithing_table_front", "right": "smithing_table_side"}
        }

        print("Rendering compound functional blocks...")
        for comp_name, faces in compound_blocks.items():
            try:
                top_data = jar.read(f"assets/minecraft/textures/block/{faces['top']}.png")
                left_data = jar.read(f"assets/minecraft/textures/block/{faces['left']}.png")
                right_data = jar.read(f"assets/minecraft/textures/block/{faces['right']}.png")

                top_im = Image.open(io.BytesIO(top_data)).convert("RGBA").resize((16, 16), Image.Resampling.NEAREST)
                left_im = Image.open(io.BytesIO(left_data)).convert("RGBA").resize((16, 16), Image.Resampling.NEAREST)
                right_im = Image.open(io.BytesIO(right_data)).convert("RGBA").resize((16, 16), Image.Resampling.NEAREST)

                top_im = apply_brightness(top_im, TOP_BRIGHTNESS)
                left_im = apply_brightness(left_im, LEFT_BRIGHTNESS)
                right_im = apply_brightness(right_im, RIGHT_BRIGHTNESS)

                canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
                transformed_top = top_im.transform((512, 512), Image.Transform.AFFINE, top_matrix, Image.Resampling.NEAREST)
                transformed_left = left_im.transform((512, 512), Image.Transform.AFFINE, left_matrix, Image.Resampling.NEAREST)
                transformed_right = right_im.transform((512, 512), Image.Transform.AFFINE, right_matrix, Image.Resampling.NEAREST)

                canvas = Image.alpha_composite(canvas, transformed_top)
                canvas = Image.alpha_composite(canvas, transformed_left)
                canvas = Image.alpha_composite(canvas, transformed_right)

                canvas.save(os.path.join(dest_dir, f"{comp_name}.png"), "PNG")
                rendered_count += 1
                print(f"Rendered compound block: {comp_name}")
            except Exception as e:
                print(f"Error rendering compound block {comp_name}: {e}")
                
    print(f"\nMass 3D generation complete! Total blocks transformed to 3D: {rendered_count}")
else:
    print("Error: Could not find JAR file.")
