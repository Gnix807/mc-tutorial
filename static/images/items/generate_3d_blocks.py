import os
import zipfile
from PIL import Image

# 3D立方体各面在32x32画布下的仿射变换逆矩阵参数 (a, b, c, d, e, f)
# x' = a*x + b*y + c, y' = d*x + e*y + f
# 这是将 16x16 像素的平面图片完美拉伸并倾斜拼装为等轴测立方体三个面的数学矩阵
left_matrix = (1.333333, 0.0, -5.333333, -0.583333, 1.0, -6.666667)
right_matrix = (1.333333, 0.0, -21.333333, 0.583333, 1.0, -25.333333)
top_matrix = (0.666667, 1.142857, -12.952381, -0.666667, 1.142857, 8.380952)

# 阴影系数 (顶面亮，左面中，右面暗，营造立体感)
TOP_BRIGHTNESS = 1.0
LEFT_BRIGHTNESS = 0.8
RIGHT_BRIGHTNESS = 0.6

# 定义需要生成 3D 立体方块的列表以及它们在 jar 包中的三个面纹理映射
blocks_to_render = {
    # 木板系列：所有面使用同一纹理
    "oak_planks": {
        "top": "oak_planks", "left": "oak_planks", "right": "oak_planks"
    },
    "spruce_planks": {
        "top": "spruce_planks", "left": "spruce_planks", "right": "spruce_planks"
    },
    "birch_planks": {
        "top": "birch_planks", "left": "birch_planks", "right": "birch_planks"
    },
    "jungle_planks": {
        "top": "jungle_planks", "left": "jungle_planks", "right": "jungle_planks"
    },
    "acacia_planks": {
        "top": "acacia_planks", "left": "acacia_planks", "right": "acacia_planks"
    },
    "dark_oak_planks": {
        "top": "dark_oak_planks", "left": "dark_oak_planks", "right": "dark_oak_planks"
    },
    "mangrove_planks": {
        "top": "mangrove_planks", "left": "mangrove_planks", "right": "mangrove_planks"
    },
    "cherry_planks": {
        "top": "cherry_planks", "left": "cherry_planks", "right": "cherry_planks"
    },
    "bamboo_planks": {
        "top": "bamboo_planks", "left": "bamboo_planks", "right": "bamboo_planks"
    },
    "crimson_planks": {
        "top": "crimson_planks", "left": "crimson_planks", "right": "crimson_planks"
    },
    "warped_planks": {
        "top": "warped_planks", "left": "warped_planks", "right": "warped_planks"
    },
    
    # 常用石头与基础方块
    "cobblestone": {
        "top": "cobblestone", "left": "cobblestone", "right": "cobblestone"
    },
    
    # 复杂功能方块
    "crafting_table": {
        "top": "crafting_table_top", 
        "left": "crafting_table_front", 
        "right": "crafting_table_side"
    },
    "furnace": {
        "top": "furnace_top", 
        "left": "furnace_front_on", # 使用开启态正面，更具动态质感
        "right": "furnace_side"
    },
    "smithing_table": {
        "top": "smithing_table_top", 
        "left": "smithing_table_front", 
        "right": "smithing_table_side"
    }
}

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
    """乘算亮度通道，营造真实立体面的阴影深浅效果"""
    if factor == 1.0:
        return im
    # 仅调整 RGB 颜色，保留原始的 A 透明度通道
    r, g, b, a = im.split()
    r = r.point(lambda p: min(255, int(p * factor)))
    g = g.point(lambda p: min(255, int(p * factor)))
    b = b.point(lambda p: min(255, int(p * factor)))
    return Image.merge("RGBA", (r, g, b, a))

jar_path = find_jar_in_folder(target_version_path)

if jar_path:
    print(f"Beginning 3D Block Rendering from game client: {jar_path}")
    rendered_count = 0
    
    with zipfile.ZipFile(jar_path, 'r') as jar:
        for block_name, faces in blocks_to_render.items():
            dest_file = f"{dest_dir}/{block_name}.png"
            
            # 读取顶、左、右三个面的平面 16x16 像素图
            try:
                top_data = jar.read(f"assets/minecraft/textures/block/{faces['top']}.png")
                left_data = jar.read(f"assets/minecraft/textures/block/{faces['left']}.png")
                right_data = jar.read(f"assets/minecraft/textures/block/{faces['right']}.png")
            except KeyError as e:
                # 兼容处理：例如 furnace_top 纹理名可能因版本不同而变化，提供备用
                try:
                    if "furnace_top" in str(e):
                        top_data = jar.read("assets/minecraft/textures/block/smooth_stone.png")
                        left_data = jar.read(f"assets/minecraft/textures/block/{faces['left']}.png")
                        right_data = jar.read(f"assets/minecraft/textures/block/{faces['right']}.png")
                    else:
                        raise e
                except KeyError:
                    print(f"Error: Missing texture for {block_name}, skipping.")
                    continue

            # 转成 Pillow 的 RGBA 图像流
            from io import BytesIO
            top_im = Image.open(BytesIO(top_data)).convert("RGBA")
            left_im = Image.open(BytesIO(left_data)).convert("RGBA")
            right_im = Image.open(BytesIO(right_data)).convert("RGBA")

            # 1. 确保源图强制为 16x16
            top_im = top_im.resize((16, 16), Image.Resampling.NEAREST)
            left_im = left_im.resize((16, 16), Image.Resampling.NEAREST)
            right_im = right_im.resize((16, 16), Image.Resampling.NEAREST)

            # 2. 对侧面进行阴影处理
            top_im = apply_brightness(top_im, TOP_BRIGHTNESS)
            left_im = apply_brightness(left_im, LEFT_BRIGHTNESS)
            right_im = apply_brightness(right_im, RIGHT_BRIGHTNESS)

            # 3. 创建 32x32 大小的透明背景图作为 3D 立方体容器
            canvas = Image.new("RGBA", (32, 32), (0, 0, 0, 0))

            # 4. 分别对待变换的三个面进行仿射投影变形，并以 RGBA 模式合并堆叠
            # Pillow.transform 采用逆矩阵公式映射源图像
            transformed_top = top_im.transform((32, 32), Image.Transform.AFFINE, top_matrix, Image.Resampling.NEAREST)
            transformed_left = left_im.transform((32, 32), Image.Transform.AFFINE, left_matrix, Image.Resampling.NEAREST)
            transformed_right = right_im.transform((32, 32), Image.Transform.AFFINE, right_matrix, Image.Resampling.NEAREST)

            # 5. 将变形完的三个面融合进主画布上
            canvas = Image.alpha_composite(canvas, transformed_top)
            canvas = Image.alpha_composite(canvas, transformed_left)
            canvas = Image.alpha_composite(canvas, transformed_right)

            # 6. 保存为 PNG 覆盖本地贴图
            canvas.save(dest_file, "PNG")
            print(f"Rendered 3D Isometric cube for: {block_name}.png")
            rendered_count += 1

    print(f"\nAll 3D block renderings completed! Rendered cubes: {rendered_count}")
else:
    print(f"Error: Game client jar not found to generate 3D cube assets.")
