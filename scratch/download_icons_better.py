import os
import re
import urllib.request
import time

file_path = 'content/docs/ch01-getting-started/04-terminology.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

img_urls = re.findall(r'<img src="(https://zh\.minecraft\.wiki/images/[^"]+)"', content)
img_urls = list(set(img_urls))

os.makedirs('static/images/icons', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://zh.minecraft.wiki/'
}

downloaded = 0
for url in img_urls:
    filename = url.split('/')[-1]
    local_path = os.path.join('static/images/icons', filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        downloaded += 1
        time.sleep(0.5)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def repl(m):
    url = m.group(1)
    filename = url.split('/')[-1]
    return f'<img src="/images/icons/{filename}"'

new_content = re.sub(r'<img src="(https://zh\.minecraft\.wiki/images/[^"]+)"', repl, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully downloaded {downloaded}/{len(img_urls)} icons.")
