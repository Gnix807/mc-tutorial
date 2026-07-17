import re

filepath = r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs\ch02-general\01-combat-and-exploration.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace ![](/images/items/X.png) with <img src="/images/items/X.png" width="64" style="image-rendering: pixelated; margin-right: 8px;" />
def repl(match):
    src = match.group(1)
    return f'<img src="{src}" width="64" style="image-rendering: pixelated; margin-right: 8px;" />'

new_content = re.sub(r'!\[\]\((/images/items/[^)]+\.png)\)', repl, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated image tags!")
