import urllib.request
import io
from PIL import Image

url = "https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c6/Shield_JE2_BE1.png"
dest = r"c:\Users\Gnix807\Desktop\新建文件夹\MC教程\static\images\items\shield.png"

try:
    print(f"Fetching from {url}...")
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
    })
    
    with urllib.request.urlopen(req, timeout=15) as response:
        data = response.read()
        
    print(f"Downloaded {len(data)} bytes. Attempting to parse as image...")
    
    # 用 PIL 强行读取内存中的图像数据
    img = Image.open(io.BytesIO(data))
    print(f"Successfully decoded image format: {img.format}, size: {img.size}")
    
    # 转换为标准的 RGBA PNG 并保存
    img = img.convert("RGBA")
    
    # 如果它的尺寸太大，我们可以稍微 resize 一下，正常应该在 16x16 或 32x32，wiki 的渲染图可能是 150x150 左右
    img.save(dest, "PNG")
    print(f"Successfully saved standard PNG to {dest}!")
    
except Exception as e:
    print(f"Failed: {e}")
