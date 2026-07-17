import os
import re

docs_dir = r"c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs"

weights = {
    "ch00-preamble": 1,
    "ch01-newcomer": 2,
    "ch02-general": 3,
    "ch03-building": 4,
    "ch04-farming": 5,
    "ch05-redstone": 6,
    "ch06-multiplayer": 7,
    "ch07-technical": 8,
}

for folder, weight in weights.items():
    idx_path = os.path.join(docs_dir, folder, "_index.md")
    if os.path.exists(idx_path):
        with open(idx_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace weight
        content = re.sub(r'weight:\s*\d+', f'weight: {weight}', content)
        
        # Add bookFlatSection and bookSectionLink if missing
        if 'bookFlatSection' not in content and folder == 'ch00-preamble':
            content = content.replace('type: docs\n---', 'type: docs\nbookFlatSection: true\nbookSectionLink: false\n---')

        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {folder} to weight {weight}")
