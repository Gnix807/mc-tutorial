import os
import re

def strip_numbering(content):
    # Match "第X章 · " or "第X章 "
    content = re.sub(r'第[一二三四五六七八九十]+章\s*·?\s*', '', content)
    return content

for root, dirs, files in os.walk('content'):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = strip_numbering(content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {filepath}")
