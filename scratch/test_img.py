from bs4 import BeautifulSoup

file_path = r'C:\Users\Gnix807\.gemini\antigravity\brain\83cd8112-7841-48bd-9577-892c92708617\.system_generated\steps\2773\content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table', class_='wikitable')
for tr in tables[1].find_all('tr'):
    if tr.find('img'):
        print(tr)
        break
