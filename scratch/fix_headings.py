import re

filepath = r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs\ch02-general\01-combat-and-exploration.md'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
current_h3 = ""

for line in lines:
    if line.startswith('## '):
        # ## 战斗 or ## 探索 -> keep as is
        new_lines.append(line)
    elif line.startswith('### '):
        # If it's a numbered section like "### 1. 战斗机制基础", it's a valid H3
        match = re.match(r'^### (\d+\.) (.*)', line)
        if match:
            new_lines.append(line)
        else:
            # It's an unnumbered sub-topic like "### 攻击指示器（冷却槽）", it should be H4
            new_lines.append(line.replace('### ', '#### ', 1))
    elif line.startswith('#### '):
        # If it's an armor like "#### 1. 皮革盔甲", it should be H5 because "盔甲速览" is now H4
        new_lines.append(line.replace('#### ', '##### ', 1))
    else:
        new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Headings fixed!")
