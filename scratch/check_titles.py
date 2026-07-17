import os
import re

content_dir = 'content/docs'
for root, _, files in os.walk(content_dir):
    for f in sorted(files):
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                match = re.search(r'^title:\s*(.*)', content, re.MULTILINE)
                if match:
                    print(f"{os.path.relpath(path, content_dir)} -> {match.group(1)}")
