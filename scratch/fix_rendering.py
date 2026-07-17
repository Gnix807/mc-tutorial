import re

with open('assets/custom.scss', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace pixelated with auto
content = content.replace('image-rendering: pixelated !important;', 'image-rendering: auto !important;')
content = content.replace('image-rendering: -moz-crisp-edges !important;', '')
content = content.replace('image-rendering: -webkit-optimize-contrast !important;', '')
content = content.replace('image-rendering: crisp-edges !important;', '')

with open('assets/custom.scss', 'w', encoding='utf-8') as f:
    f.write(content)
