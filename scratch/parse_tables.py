from bs4 import BeautifulSoup
import json

file_path = r'C:\Users\Gnix807\.gemini\antigravity\brain\83cd8112-7841-48bd-9577-892c92708617\.system_generated\steps\2773\content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', class_='wikitable')
results = []
for i, table in enumerate(tables):
    rows = []
    for tr in table.find_all('tr'):
        cells = [td.get_text(strip=True, separator=' ') for td in tr.find_all(['th', 'td'])]
        rows.append(cells)
    results.append(rows)

with open('scratch/tables.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(tables)} tables")
