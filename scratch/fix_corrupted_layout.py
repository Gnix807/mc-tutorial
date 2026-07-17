import re

filepath = r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs\ch02-general\01-combat-and-exploration.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The file currently has lines like this:
# <img src="/images/items/iron_helmet.png" width="64" style="image-rendering: pixelated; margin-right: 8px;" /> <div class="mc-crafting-slot" data-tooltip-title="铁胸甲" data-tooltip-subtitle="护甲值: +6"><img src="/images/items/iron_chestplate.png" style="image-rendering: pixelated; width: 64px; height: 64px;" /></div> <div class="mc-crafting-slot" data-tooltip-title="铁护腿" data-tooltip-subtitle="护甲值: +5"><img src="/images/items/iron_leggings.png" style="image-rendering: pixelated; width: 64px; height: 64px;" /></div> <div class="mc-crafting-slot" data-tooltip-title="铁靴子" data-tooltip-subtitle="护甲值: +2"><img src="/images/items/iron_boots.png" style="image-rendering: pixelated; width: 64px; height: 64px;" /></div>
# </div>

# Let's write a more robust regex that just finds ALL <img src="..."> on the line after #### and rewrites the whole block.
def fix_armor_block(match):
    header = match.group(1)
    block_content = match.group(2)
    
    # Extract all image srcs
    srcs = re.findall(r'<img[^>]*?src="([^"]+)"[^>]*?>', block_content)
    
    imgs = []
    for src in srcs:
        imgs.append(f'<img src="{src}" width="64" style="image-rendering: pixelated; margin-right: 8px;" />')
    
    # Return the header followed by the clean images on the next line
    return header + "\n" + " ".join(imgs) + "\n"

# Match from #### ... to the line before - **护甲值
# We will match the #### header, and everything up to the </div> or just before the bullet point
content = re.sub(r'(#### \d+\.\s+.*?\n)(.*?)\n-', lambda m: fix_armor_block(m) + "-", content, flags=re.DOTALL)

# Also ensure no trailing </div> is left
content = re.sub(r'</div>\n-', '-', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed layout!")
