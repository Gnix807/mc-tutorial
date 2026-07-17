import urllib.request
from bs4 import BeautifulSoup

url = "https://zh.minecraft.wiki/w/Tutorial:%E8%AE%A1%E9%87%8F%E5%8D%95%E4%BD%8D"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        # get text inside mw-parser-output
        content = soup.find(class_="mw-parser-output")
        if content:
            print(content.get_text(separator='\n', strip=True)[:1000])
        else:
            print("Could not find content")
except Exception as e:
    print("Error:", e)
