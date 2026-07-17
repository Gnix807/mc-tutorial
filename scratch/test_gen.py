from bs4 import BeautifulSoup
import urllib.parse

file_path = r'C:\Users\Gnix807\.gemini\antigravity\brain\83cd8112-7841-48bd-9577-892c92708617\.system_generated\steps\2773\content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table', class_='wikitable')

def html_to_md_table(table_html):
    md = []
    rows = table_html.find_all('tr')
    for i, row in enumerate(rows):
        cells = row.find_all(['th', 'td'])
        
        cleaned_cells = []
        for cell in cells:
            # We want to keep images but turn them into HTML <img src="..."> 
            # First, process list items
            lis = cell.find_all('li')
            if lis:
                for li in lis:
                    # we need to extract contents of li
                    pass # handled below
                    
            # Let's replace images with a special placeholder or just build text
            # Actually, we can replace the img element itself in the soup
            for img in cell.find_all('img'):
                src = img.get('src', '')
                # remove query string
                src = src.split('?')[0]
                if src.startswith('/images'):
                    src = 'https://zh.minecraft.wiki' + src
                # create a new string to replace the img
                new_img = f'<img src="{src}" width="16" style="vertical-align: middle; display: inline-block; image-rendering: pixelated; margin-right: 4px;">'
                img.replace_with(soup.new_string(new_img))
                
            # Now we get text but we want the raw string of the cell so our <img> strings remain
            # Actually, soup.new_string escapes HTML. We should just parse cell inner HTML or iterate contents
            cell_text = ""
            for child in cell.contents:
                if child.name == 'ul':
                    items = []
                    for li in child.find_all('li'):
                        items.append(li.get_text(strip=True).replace('&lt;', '<').replace('&gt;', '>'))
                    cell_text += "，".join(items)
                else:
                    if hasattr(child, 'get_text'):
                        text = child.get_text(strip=True)
                    else:
                        text = str(child).strip()
                    
                    # Wait, if we mutated child (img), getting text might not give us the new_img string if it was escaped.
                    pass
                    
    return md

