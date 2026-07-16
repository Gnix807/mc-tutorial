import os
import urllib.request
import time

# 待补全的贴图列表以及它们在 GitHub 官方解包库中的类型 (item 还是 block)
github_items = {
    "diamond": "item",
    "wooden_shovel": "item",
    "wooden_axe": "item",
    "iron_sword": "item",
    "diamond_shovel": "item",
    "diamond_axe": "item",
    "diamond_hoe": "item",
    "netherite_pickaxe": "item",
    "netherite_hoe": "item",
    "smithing_table": "block" # 备用：如果 Wiki 的 3D 渲染图失败，下载平铺的方块图作为后备
}

dest_dir = "static/images/items"
proxy = "http://127.0.0.1:7897"

# 注入本地代理
os.environ['HTTP_PROXY'] = proxy
os.environ['HTTPS_PROXY'] = proxy

def download_file(url, filepath):
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"Error downloading from {url}: {e}")
        return False

# 1. 尝试下载 3D 锻造台和钻石的 Wiki 图片
print("Attempting to get Smithing Table 3D render and Diamond from Minecraft Wiki...")
download_file("https://minecraft.wiki/images/Smithing_Table.png", f"{dest_dir}/smithing_table.png")
download_file("https://minecraft.wiki/images/Diamond_JE3_BE3.png", f"{dest_dir}/diamond.png")
# 备用 Wiki 钻石命名试探
if not os.path.exists(f"{dest_dir}/diamond.png") or os.path.getsize(f"{dest_dir}/diamond.png") < 500:
    download_file("https://minecraft.wiki/images/Diamond_JE3_BE2.png", f"{dest_dir}/diamond.png")

# 2. 从 GitHub 官方解包库拉取所有依旧是占位图的工具贴图
for key, category in github_items.items():
    filepath = f"{dest_dir}/{key}.png"
    
    # 只有当贴图依旧是占位符（大小 < 500 字节，占位符为 79 字节）时才去下载
    if os.path.exists(filepath) and os.path.getsize(filepath) > 500:
        print(f"Skipping {key}.png (already downloaded and verified)")
        continue

    print(f"Downloading official texture for {key}.png from GitHub...")
    # 构建 GitHub 官方解包源 URL
    url = f"https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.20.1/assets/minecraft/textures/{category}/{key}.png"
    
    # 针对 smithing_table 这种方块，官方解包的 block 贴图是 flat 的，如果是 smithing_table 则尝试使用 smithing_table_front 作为贴图
    if key == "smithing_table" and category == "block":
        url = "https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.20.1/assets/minecraft/textures/block/smithing_table_front.png"

    success = download_file(url, filepath)
    if success:
        print(f"Successfully补全贴图: {key}.png")
    else:
        print(f"Failed to補全贴图: {key}.png")
        
    time.sleep(0.1)

print("All asset supplementary downloads completed!")
