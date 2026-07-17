import re

with open('assets/custom.scss', 'r', encoding='utf-8') as f:
    content = f.read()

# mc-crafting-grid
content = re.sub(r'grid-template-columns:\s*repeat\(3,\s*88px\);', 'grid-template-columns: repeat(3, 104px);', content)
content = re.sub(r'grid-template-rows:\s*repeat\(3,\s*88px\);', 'grid-template-rows: repeat(3, 104px);', content)

# mc-crafting-slot
content = re.sub(r'\.mc-crafting-slot\s*\{\s*position:\s*relative;\s*flex-shrink:\s*0;\s*width:\s*88px;\s*height:\s*88px;', '.mc-crafting-slot {\n  position: relative;\n  flex-shrink: 0;\n  width: 104px;\n  height: 104px;', content)

# mc-crafting-slot img
content = re.sub(r'width:\s*80px\s*!important;\s*height:\s*80px\s*!important;', 'width: 96px !important;\n    height: 96px !important;', content)

# mc-crafting-arrow
content = re.sub(r'\.mc-crafting-arrow\s*\{\s*width:\s*66px;\s*flex-shrink:\s*0;\s*height:\s*44px;', '.mc-crafting-arrow {\n  width: 78px;\n  flex-shrink: 0;\n  height: 52px;', content)

with open('assets/custom.scss', 'w', encoding='utf-8') as f:
    f.write(content)
