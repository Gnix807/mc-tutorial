import re

with open('content/docs/ch02-general/01-combat-and-exploration.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace width: 64px; height: 64px; inline styles in the markdown
content = re.sub(r'style="image-rendering:\s*pixelated;\s*width:\s*64px;\s*height:\s*64px;"', '', content)
# Also clean up empty style attributes just in case
content = re.sub(r'\s*style=""', '', content)

with open('content/docs/ch02-general/01-combat-and-exploration.md', 'w', encoding='utf-8') as f:
    f.write(content)
