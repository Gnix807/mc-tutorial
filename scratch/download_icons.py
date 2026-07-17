import os
import re
import urllib.request

file_path = 'content/docs/ch01-getting-started/04-terminology.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all <img src="..."> 
img_urls = re.findall(r'<img src="(https://zh\.minecraft\.wiki/images/[^"]+)"', content)
img_urls = list(set(img_urls))

os.makedirs('static/images/icons', exist_ok=True)

for url in img_urls:
    # URL might have ? query params but we stripped them earlier during generation
    filename = url.split('/')[-1]
    local_path = os.path.join('static/images/icons', filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Replace URLs in markdown with local paths
def repl(m):
    url = m.group(1)
    filename = url.split('/')[-1]
    return f'<img src="/images/icons/{filename}"'

new_content = re.sub(r'<img src="(https://zh\.minecraft\.wiki/images/[^"]+)"', repl, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Downloaded {len(img_urls)} icons and updated markdown.")
