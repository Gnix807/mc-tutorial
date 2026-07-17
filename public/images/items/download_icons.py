import os
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

items = {
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
    "wooden_pickaxe": "Wooden_Pickaxe",
    "stone_pickaxe": "Stone_Pickaxe",
    "iron_pickaxe": "Iron_Pickaxe",
    "wooden_shovel": "Wooden_Shovel",
    "stone_shovel": "Stone_Shovel",
    "iron_shovel": "Iron_Shovel",
    "wooden_axe": "Wooden_Axe",
    "stone_axe": "Stone_Axe",
    "iron_axe": "Iron_Axe",
    "wooden_sword": "Wooden_Sword",
    "stone_sword": "Stone_Sword",
    "iron_sword": "Iron_Sword",
    "wooden_hoe": "Wooden_Hoe",
    "stone_hoe": "Stone_Hoe",
    "iron_hoe": "Iron_Hoe",
    "furnace": "Furnace",
    "crafting_table": "Crafting_Table"
}

dest_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(dest_dir, exist_ok=True)

def download_one(key, wiki_name):
    url = f"https://minecraft.wiki/images/{wiki_name}.png"
    dest_file = os.path.join(dest_dir, f"{key}.png")
    
    # If already downloaded and size > 0, skip
    if os.path.exists(dest_file) and os.path.getsize(dest_file) > 0:
        print(f"Skipping {key}.png (already exists)")
        return
        
    print(f"Downloading {key}.png from {url}...")
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            with open(dest_file, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Success: {key}.png saved.")
    except Exception as e:
        print(f"Error downloading {key}.png: {e}")

# Kill previous downloads by deleting locking/incomplete files or just let it overwrite
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(download_one, k, v) for k, v in items.items()]
    for f in futures:
        f.result()

# Generate empty 1x1 transparent PNG
empty_file = os.path.join(dest_dir, "empty.png")
if not os.path.exists(empty_file):
    import base64
    # 1x1 transparent PNG base64
    transparent_png = b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='
    with open(empty_file, 'wb') as f:
        f.write(base64.b64decode(transparent_png))
    print("Created empty.png")
