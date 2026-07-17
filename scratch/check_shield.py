import zipfile
jar_path = r"E:\BaiduNetdiskDownload\Earth3 ver0.21fix\.minecraft\versions\26.2\26.2.jar"
with zipfile.ZipFile(jar_path, 'r') as zf:
    for name in zf.namelist():
        if "shield" in name.lower() and name.endswith(".png"):
            print(name)
