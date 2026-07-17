import urllib.request

url = "https://raw.githubusercontent.com/PrismarineJS/minecraft-assets/master/data/1.20.1/items/shield.png"
dest = r"c:\Users\Gnix807\Desktop\新建文件夹\MC教程\static\images\items\shield.png"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = response.read()
        if len(data) > 200: # 确保不是报错文件
            with open(dest, 'wb') as out_file:
                out_file.write(data)
            print("Successfully downloaded shield.png from PrismarineJS!")
        else:
            print("Data too small.")
except Exception as e:
    print(f"Error: {e}")
