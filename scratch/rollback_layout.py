import re

filepath = r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs\ch02-general\01-combat-and-exploration.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert the mc-gui-panel blocks for the 4 armors
def revert_panel(match):
    panel_content = match.group(1)
    # Extract all img srcs
    srcs = re.findall(r'<img[^>]*?src="([^"]+)"[^>]*?>', panel_content)
    
    imgs = []
    for src in srcs:
        imgs.append(f'<img src="{src}" width="64" style="image-rendering: pixelated; margin-right: 8px;" />')
    return " ".join(imgs)

content = re.sub(r'<div class="mc-gui-panel">\s*(.*?)\s*</div>', revert_panel, content, flags=re.DOTALL)

# 2. Revert the inline turtle shell
def revert_inline(match):
    src = match.group(1)
    return f'<img src="{src}" width="64" style="image-rendering: pixelated; margin-right: 8px;" />'

content = re.sub(r'<span class="mc-crafting-slot"[^>]*?>\s*<img[^>]*?src="([^"]+)"[^>]*?>\s*</span>', revert_inline, content)

# 3. Remove the tooltip script at the bottom
content = re.sub(r'<script>.*?mc-crafting-tooltip.*?</script>', '', content, flags=re.DOTALL)
# cleanup extra newlines at the end
content = content.strip() + '\n'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Rollback complete!")
