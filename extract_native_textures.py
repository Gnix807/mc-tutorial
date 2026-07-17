import zipfile
import os
import shutil

jar_path = r"E:\BaiduNetdiskDownload\Earth3 ver0.21fix\.minecraft\versions\26.2\26.2.jar"
dest_dir = r"c:\Users\Gnix807\Desktop\新建文件夹\MC教程\static\images\items"

os.makedirs(dest_dir, exist_ok=True)

extracted_count = 0

with zipfile.ZipFile(jar_path, 'r') as zf:
    # 提取方块和物品，为了防止重名覆盖（如部分特殊物品），让 item 的优先级高于 block
    # 因此先解压 block，再解压 item
    
    # 1. 解压方块贴图
    for member in zf.infolist():
        if member.is_dir() or not member.filename.endswith(".png"):
            continue
        if member.filename.startswith("assets/minecraft/textures/block/"):
            filename = os.path.basename(member.filename)
            target_path = os.path.join(dest_dir, filename)
            with zf.open(member.filename) as source, open(target_path, "wb") as target:
                shutil.copyfileobj(source, target)
            extracted_count += 1
            
    # 2. 解压物品贴图
    for member in zf.infolist():
        if member.is_dir() or not member.filename.endswith(".png"):
            continue
        if member.filename.startswith("assets/minecraft/textures/item/"):
            filename = os.path.basename(member.filename)
            target_path = os.path.join(dest_dir, filename)
            with zf.open(member.filename) as source, open(target_path, "wb") as target:
                shutil.copyfileobj(source, target)
            extracted_count += 1

print(f"Extraction complete! Successfully extracted {extracted_count} native textures to {dest_dir}.")
