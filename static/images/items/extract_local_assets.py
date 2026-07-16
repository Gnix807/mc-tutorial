import os
import zipfile

# 用户指定的版本文件夹
target_version_path = r"E:\BaiduNetdiskDownload\Earth3 ver0.21fix\.minecraft\versions\26.2"
dest_dir = "static/images/items"

# 确保目标文件夹存在
os.makedirs(dest_dir, exist_ok=True)

def find_jar_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: Directory not found at {folder_path}")
        return None
        
    for file in os.listdir(folder_path):
        if file.endswith(".jar"):
            jar_path = os.path.join(folder_path, file)
            if os.path.getsize(jar_path) > 5 * 1024 * 1024:
                return jar_path
                
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jar"):
                jar_path = os.path.join(root, file)
                if os.path.getsize(jar_path) > 5 * 1024 * 1024:
                    return jar_path
                    
    return None

print(f"Scanning target folder: {target_version_path}...")
jar_path = find_jar_in_folder(target_version_path)

if jar_path:
    print(f"Found game .jar client: {jar_path}")
    block_count = 0
    item_count = 0
    try:
        with zipfile.ZipFile(jar_path, 'r') as jar:
            for file_info in jar.infolist():
                filename = file_info.filename
                
                # 只过滤 png 图片文件
                if filename.endswith(".png"):
                    # 1. 方块贴图: assets/minecraft/textures/block/*.png (限制斜杠数等于4以过滤顶层文件，避开子目录)
                    if filename.startswith("assets/minecraft/textures/block/") and filename.count("/") == 4:
                        base_name = os.path.basename(filename)
                        dest_file = os.path.join(dest_dir, base_name)
                        
                        data = jar.read(filename)
                        with open(dest_file, "wb") as f:
                            f.write(data)
                        block_count += 1
                        
                    # 2. 物品贴图: assets/minecraft/textures/item/*.png (同上，平铺展开)
                    elif filename.startswith("assets/minecraft/textures/item/") and filename.count("/") == 4:
                        base_name = os.path.basename(filename)
                        dest_file = os.path.join(dest_dir, base_name)
                        
                        data = jar.read(filename)
                        with open(dest_file, "wb") as f:
                            f.write(data)
                        item_count += 1
                        
        print(f"\nAll Minecraft official textures extracted successfully!")
        print(f"Total Block textures extracted: {block_count}")
        print(f"Total Item textures extracted: {item_count}")
        print(f"Total textures now available offline in: {dest_dir}")
    except Exception as e:
        print(f"Error reading JAR file: {e}")
else:
    print(f"Error: Could not find any valid client .jar files in {target_version_path}")
