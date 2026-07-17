import re

with open('assets/custom.scss', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace img properties in mc-crafting-slot
replacement_slot = '''  img {
    box-sizing: content-box !important;
    width: 80px !important;
    height: 80px !important;
    padding: 0 !important;
    margin: 0 !important;
    border: none !important;
    max-width: none !important;
    max-height: none !important;
    flex-shrink: 0 !important;
    object-fit: fill !important;
    image-rendering: -moz-crisp-edges !important;
    image-rendering: -webkit-optimize-contrast !important;
    image-rendering: crisp-edges !important;
    image-rendering: pixelated !important;
    transition: opacity 0.15s ease-in-out;
  }'''

content = re.sub(r'img\s*\{[^}]*width:\s*80px;[^}]*\}', replacement_slot, content)

# Replace img properties in mc-crafting-result-slot
replacement_result = '''  img {
    box-sizing: content-box !important;
    width: 128px !important;
    height: 128px !important;
    padding: 0 !important;
    margin: 0 !important;
    border: none !important;
    max-width: none !important;
    max-height: none !important;
    flex-shrink: 0 !important;
    object-fit: fill !important;
    image-rendering: -moz-crisp-edges !important;
    image-rendering: -webkit-optimize-contrast !important;
    image-rendering: crisp-edges !important;
    image-rendering: pixelated !important;
    transition: opacity 0.15s ease-in-out;
  }'''

content = re.sub(r'img\s*\{[^}]*width:\s*128px;[^}]*\}', replacement_result, content)

with open('assets/custom.scss', 'w', encoding='utf-8') as f:
    f.write(content)
