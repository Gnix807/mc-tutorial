import urllib.request

urls = [
    "https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c6/Shield_JE2_BE1.png",
    "https://raw.githubusercontent.com/PrismarineJS/minecraft-assets/master/data/1.20/items/shield.png",
    "https://raw.githubusercontent.com/PrismarineJS/minecraft-assets/master/data/1.19.4/items/shield.png",
    "https://raw.githubusercontent.com/PrismarineJS/minecraft-assets/master/data/1.18.2/items/shield.png",
    "https://raw.githubusercontent.com/InventivetalentDev/minecraft-assets/1.18.2/assets/minecraft/textures/item/shield.png"
]

dest = r"c:\Users\Gnix807\Desktop\新建文件夹\MC教程\static\images\items\shield.png"
success = False

for url in urls:
    print(f"Trying {url}...")
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
            # Check if it's a valid PNG (starts with \x89PNG) and isn't HTML
            if data.startswith(b"\x89PNG") and b"<!DOCTYPE html>" not in data:
                with open(dest, 'wb') as out_file:
                    out_file.write(data)
                print("Success!")
                success = True
                break
            else:
                print("Invalid image data.")
    except Exception as e:
        print(f"Failed: {e}")

if not success:
    print("All downloads failed.")
