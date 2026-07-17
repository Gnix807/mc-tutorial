import urllib.request
import os
import sys

# 尝试多个可能的图标链接
urls = [
    "https://zh.minecraft.wiki/images/Shield.png",
    "https://minecraft.wiki/images/Shield.png",
    "https://zh.minecraft.wiki/images/Shield_%28item%29.png"
]
dest = r"c:\Users\Gnix807\Desktop\新建文件夹\MC教程\static\images\items\shield.png"

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
            data = response.read()
            if len(data) > 100:  # 确保不是个空文件或者错误页面
                out_file.write(data)
                print(f"Success! Downloaded from {url}")
                sys.exit(0)
    except Exception as e:
        print(f"Failed for {url}: {e}")

print("Could not download shield.png")
sys.exit(1)
