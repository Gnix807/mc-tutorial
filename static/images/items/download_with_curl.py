import os
import subprocess
import time

# 完美映射 Wiki 上的真实图片名称（避开 1.14 材质更新带来的 JE2/JE3/BE2 等历史后缀 404 问题）
items = {
    # 木板与基础材料
    "oak_planks": "Oak_Planks",
    "spruce_planks": "Spruce_Planks",
    "birch_planks": "Birch_Planks",
    "jungle_planks": "Jungle_Planks",
    "acacia_planks": "Acacia_Planks",
    "dark_oak_planks": "Dark_Oak_Planks",
    "mangrove_planks": "Mangrove_Planks",
    "cherry_planks": "Cherry_Planks",
    "bamboo_planks": "Bamboo_Planks",
    "crimson_planks": "Crimson_Planks",
    "warped_planks": "Warped_Planks",
    "stick": "Stick",
    "coal": "Coal",
    "charcoal": "Charcoal",
    "cobblestone": "Cobblestone",
    "raw_iron": "Raw_Iron",
    "iron_ingot": "Iron_Ingot",
    "diamond": "Diamond_JE3_BE3",
    "netherite_ingot": "Netherite_Ingot_JE2_BE1",
    "netherite_upgrade_smithing_template": "Netherite_Upgrade_Smithing_Template",
    "smithing_table": "Smithing_Table",

    # 木质工具
    "wooden_pickaxe": "Wooden_Pickaxe",
    "wooden_shovel": "Wooden_Shovel_JE3_BE2",
    "wooden_axe": "Wooden_Axe_JE3_BE2",
    "wooden_sword": "Wooden_Sword_JE2_BE2",
    "wooden_hoe": "Wooden_Hoe_JE3_BE2",

    # 石质工具
    "stone_pickaxe": "Stone_Pickaxe",
    "stone_shovel": "Stone_Shovel",
    "stone_axe": "Stone_Axe",
    "stone_sword": "Stone_Sword",
    "stone_hoe": "Stone_Hoe_JE2_BE2",

    # 铁质工具
    "iron_pickaxe": "Iron_Pickaxe",
    "iron_shovel": "Iron_Shovel",
    "iron_axe": "Iron_Axe_JE6_BE2",
    "iron_sword": "Iron_Sword_JE2_BE2",
    "iron_hoe": "Iron_Hoe_JE2_BE2",

    # 钻石工具
    "diamond_pickaxe": "Diamond_Pickaxe_JE3_BE3",
    "diamond_shovel": "Diamond_Shovel_JE3_BE2",
    "diamond_axe": "Diamond_Axe_JE3_BE2",
    "diamond_sword": "Diamond_Sword_JE3_BE2",
    "diamond_hoe": "Diamond_Hoe_JE2_BE2",

    # 下界合金工具
    "netherite_pickaxe": "Netherite_Pickaxe_JE2",
    "netherite_shovel": "Netherite_Shovel_JE2",
    "netherite_axe": "Netherite_Axe_JE2",
    "netherite_sword": "Netherite_Sword_JE2",
    "netherite_hoe": "Netherite_Hoe_JE2",

    # 功能方块
    "furnace": "Furnace",
    "crafting_table": "Crafting_Table"
}

dest_dir = "static/images/items"
proxy = "http://127.0.0.1:7897"

# 确保文件夹存在
os.makedirs(dest_dir, exist_ok=True)

for key, wiki_name in items.items():
    dest_file = f"{dest_dir}/{key}.png"
    
    # 只要文件已经有内容且大小 > 500 字节，就跳过
    if os.path.exists(dest_file) and os.path.getsize(dest_file) > 500:
        print(f"Skipping {key}.png (already exists and looks real)")
        continue

    url = f"https://minecraft.wiki/images/{wiki_name}.png"
    print(f"Downloading {key}.png via curl to relative path {dest_file}...")
    
    # 限制连接 10s，最大耗时 35s
    cmd = [
        "curl",
        "-L",
        "-s",
        "--connect-timeout", "10",
        "--max-time", "35",
        "--proxy", proxy,
        "-o", dest_file,
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        url
    ]
    
    try:
        result = subprocess.run(cmd)
        if result.returncode == 0 and os.path.exists(dest_file) and os.path.getsize(dest_file) > 500:
            print(f"Successfully downloaded {key}.png")
        else:
            print(f"Minecraft Wiki source failed for {key}.png")
    except Exception as e:
        print(f"Error executing curl for {key}.png: {e}")
    
    time.sleep(0.1)
