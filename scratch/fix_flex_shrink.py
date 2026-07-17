import re

with open('assets/custom.scss', 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex-shrink: 0 to mc-crafting-grid
content = re.sub(r'(\.mc-crafting-grid\s*\{\s*display:\s*grid;)', r'\1\n  flex-shrink: 0;', content)

# Add flex-shrink: 0 to mc-crafting-slot
content = re.sub(r'(\.mc-crafting-slot\s*\{\s*position:\s*relative;)', r'\1\n  flex-shrink: 0;', content)

# Add flex-shrink: 0 to mc-crafting-arrow
content = re.sub(r'(\.mc-crafting-arrow\s*\{\s*width:\s*66px;)', r'\1\n  flex-shrink: 0;', content)

# Add flex-shrink: 0 to mc-crafting-result-slot
content = re.sub(r'(\.mc-crafting-result-slot\s*\{\s*width:\s*140px;)', r'\1\n  flex-shrink: 0;', content)

# Ensure img does not get squished
content = re.sub(r'(img\s*\{[^}]*width:\s*80px;\s*height:\s*80px;)', r'\1\n    max-width: none;\n    max-height: none;\n    flex-shrink: 0;', content)
content = re.sub(r'(img\s*\{[^}]*width:\s*128px;\s*height:\s*128px;)', r'\1\n    max-width: none;\n    max-height: none;\n    flex-shrink: 0;', content)

with open('assets/custom.scss', 'w', encoding='utf-8') as f:
    f.write(content)
