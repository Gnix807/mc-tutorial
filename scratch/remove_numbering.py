import re

filepath = 'content/_index.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "[X.Y " with "["
content = re.sub(r'\[\d+\.\d+\s+', '[', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed numbering from _index.md")
