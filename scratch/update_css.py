import re

with open('assets/custom.scss', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'grid-template-columns:\s*repeat\(3,\s*72px\);', 'grid-template-columns: repeat(3, 88px);', content)
content = re.sub(r'grid-template-rows:\s*repeat\(3,\s*72px\);', 'grid-template-rows: repeat(3, 88px);', content)
content = re.sub(r'gap:\s*6px;', 'gap: 8px;', content)
content = re.sub(r'\.mc-crafting-slot\s*\{\s*position:\s*relative;\s*width:\s*72px;\s*height:\s*72px;', '.mc-crafting-slot {\n  position: relative;\n  width: 88px;\n  height: 88px;', content)
content = re.sub(r'width:\s*64px;\s*height:\s*64px;\s*object-fit:\s*contain;\s*image-rendering:\s*pixelated;', 'width: 80px;\n    height: 80px;\n    object-fit: contain;\n    image-rendering: -moz-crisp-edges;\n    image-rendering: -webkit-optimize-contrast;\n    image-rendering: crisp-edges;\n    image-rendering: pixelated;', content)
content = re.sub(r'\.mc-crafting-arrow\s*\{\s*width:\s*54px;\s*height:\s*36px;', '.mc-crafting-arrow {\n  width: 66px;\n  height: 44px;', content)
content = re.sub(r'\.mc-crafting-result-slot\s*\{\s*width:\s*108px;\s*height:\s*108px;', '.mc-crafting-result-slot {\n  width: 140px;\n  height: 140px;', content)
content = re.sub(r'width:\s*96px;\s*height:\s*96px;\s*object-fit:\s*contain;\s*image-rendering:\s*pixelated;', 'width: 128px;\n    height: 128px;\n    object-fit: contain;\n    image-rendering: -moz-crisp-edges;\n    image-rendering: -webkit-optimize-contrast;\n    image-rendering: crisp-edges;\n    image-rendering: pixelated;', content)
content = re.sub(r'font-size:\s*18px;', 'font-size: 24px;', content)
content = re.sub(r'padding:\s*6px\s*12px;\s*font-size:\s*13px;', 'padding: 8px 16px;\n  font-size: 16px;', content)
content = re.sub(r'font-size:\s*11px;\s*display:\s*block;\s*margin-top:\s*2px;', 'font-size: 14px;\n    display: block;\n    margin-top: 4px;', content)

with open('assets/custom.scss', 'w', encoding='utf-8') as f:
    f.write(content)
