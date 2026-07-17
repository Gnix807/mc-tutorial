from bs4 import BeautifulSoup
import re

file_path = r'C:\Users\Gnix807\.gemini\antigravity\brain\83cd8112-7841-48bd-9577-892c92708617\.system_generated\steps\2773\content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table', class_='wikitable')

def html_to_md_table(table_html):
    md = []
    rows = table_html.find_all('tr')
    for i, row in enumerate(rows):
        cells = row.find_all(['th', 'td'])
        
        cleaned_cells = []
        for cell in cells:
            # Replace imgs with raw html string placeholders
            for img in cell.find_all('img'):
                src = img.get('src', '')
                src = src.split('?')[0]
                if src.startswith('/images'):
                    src = 'https://zh.minecraft.wiki' + src
                # Create a placeholder string that we won't strip
                placeholder = f' ℑ{src}ℑ '
                img.replace_with(placeholder)

            # Get text
            # Handle ul/li by replacing ul with joined li
            for ul in cell.find_all('ul'):
                items = [li.get_text(strip=True) for li in ul.find_all('li')]
                ul.replace_with('，'.join(items))

            text = cell.get_text(strip=True, separator=' ')
            
            # Now replace the placeholder back with HTML
            # Need to be careful with markdown table escaping
            def repl(m):
                s = m.group(1)
                return f'<img src="{s}" width="16" style="vertical-align: middle; display: inline-block; image-rendering: pixelated; margin-right: 4px;">'
            
            text = re.sub(r'ℑ(.*?)ℑ', repl, text)
            
            # Clean up newlines and pipes
            text = text.replace('\n', ' ').replace('|', '\|')
            cleaned_cells.append(text.strip())
            
        md_row = "| " + " | ".join(cleaned_cells) + " |"
        md.append(md_row)
        
        if i == 0:
            md.append("| " + " | ".join(["---"] * len(cleaned_cells)) + " |")
            
    return '\n'.join(md)

zh_table_md = html_to_md_table(tables[1])

en_terms = '''| 英文术语 | 中文译名 | 术语定义 |
| --- | --- | --- |
| Admin / OP | 管理员 / 操作员 | OP是Operator的简称，指在服务器中拥有特权指令的管理员玩家。 |
| AFK | 挂机 | Away From Keyboard（把手离开键盘）的缩写，指玩家挂机不操作。 |
| Buff / Debuff | 增益 / 减益状态 | 指游戏中的正面状态效果（如力量、速度）和负面状态效果（如中毒、缓慢）。 |
| GG | 打得不错 | Good Game的缩写，常在多人游戏对局结束后发送，表示友好或称赞。 |
| Grief / Griefer | 破坏 / 熊孩子 | 未经允许恶意破坏他人建筑成果的行为，进行此行为的玩家常被称为“熊孩子”。 |
| Vanilla | 原版 / 纯净版 | 指原汁原味、没有安装任何Mod的Minecraft。 |
| Seed | 种子 | 用于生成世界的一串代码，相同的种子会生成完全相同的地形。 |
| Spawn | 出生点 / 生成 | 玩家进入世界时的地点，或指生物在世界中自然产生的过程。 |
| Mod | 模组 | Modification的缩写，玩家制作的游戏修改扩展包，能添加新物品或改变玩法。 |
'''

final_md = f'''---
title: 游戏术语
weight: 4
type: docs
---

# 游戏术语

在 Minecraft 的社区交流、多人游戏联机以及观看教程视频时，你可能会遇到很多“黑话”或专有术语。了解这些常用词汇，能帮助你更快地融入玩家圈子。

本页面整理了中文社区和英文社区最常使用的游戏术语。

## 常用英文术语与缩写

在多人服务器或观看国外博主的视频时，这些英文缩写极其常见：

{en_terms}

## 中文社区常用术语表

以下是国内 Minecraft 玩家在交流时最常使用的中文“黑话”与俗称。熟悉它们可以让你在看攻略或与人聊天时不再一头雾水。

{zh_table_md}

> **提示**：随着游戏版本的更新和社区的发展，术语表也在不断扩充。如果在游戏中遇到了不懂的词，随时可以查阅此表或向其他老玩家请教！
'''

out_path = 'content/docs/ch01-getting-started/04-terminology.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(final_md)

print("Icons added!")
