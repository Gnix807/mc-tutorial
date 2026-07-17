import re

filepath = r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs\ch02-general\01-combat-and-exploration.md'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith('<img src="/images/items/'):
        # It's a full block of 4 armor pieces
        # Replace each img with a slot
        def repl(match):
            src = match.group(1)
            return f'<div class="mc-crafting-slot"><img src="{src}" style="image-rendering: pixelated; width: 64px; height: 64px;" /></div>'
        
        inner = re.sub(r'<img src="([^"]+)"[^>]+>', repl, line)
        new_line = f'<div style="display: flex; gap: 8px; margin-bottom: 12px;">\n{inner.strip()}\n</div>\n'
        new_lines.append(new_line)
    elif "turtle_helmet" in line:
        # It's an inline image
        def repl_inline(match):
            src = match.group(1)
            return f'<span class="mc-crafting-slot" style="display: inline-flex; vertical-align: middle; width: 48px; height: 48px; margin: 0 4px;"><img src="{src}" style="image-rendering: pixelated; width: 40px; height: 40px;" /></span>'
        new_line = re.sub(r'<img src="([^"]+)"[^>]+>', repl_inline, line)
        new_lines.append(new_line)
    else:
        new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Wrapped in slots!")
