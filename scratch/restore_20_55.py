import re
import subprocess

# Read current file (which is at a122bc0)
filepath = r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs\ch02-general\01-combat-and-exploration.md'
with open(filepath, 'r', encoding='utf-8') as f:
    current_content = f.read()

# Get a517bf9 file content
process = subprocess.Popen(['git', 'show', 'a517bf9:content/docs/ch02-general/01-combat-and-exploration.md'], 
                           cwd=r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程',
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
a517bf9_content = stdout.decode('utf-8', errors='ignore')

# Extract the HTML layout from a517bf9_content
# It starts at "#### 1. 皮革盔甲 (Leather Armor)" and ends before "### 3. 近战实战技巧"
# But wait, in a517bf9 it was followed by "### 后勤补给". Let's match from #### 1. to the end of #### 4...
match = re.search(r'(#### 1\. 皮革盔甲.*?)(?=\n> \[!NOTE\])', a517bf9_content, re.DOTALL)
if match:
    html_layout = match.group(1)
    
    # In current_content, we want to replace the table under "### 盔甲速览"
    # The table is:
    # | 材质 | 护甲值（全套） | 耐久 | 获取难度 |
    # |---|---|---|---|
    # | 皮革 | 7 | 低 | 杀牛 |
    # | 铁 | 15 | 中 | 挖矿后烧炼 |
    # | 钻石 | 20 | 高 | 深层挖矿 |
    # | 下界合金 | 20（+击退抗性） | 极高 | 远古残骸+锻造台 |
    
    table_pattern = r'\| 材质 \| 护甲值（全套）.*?远古残骸\+锻造台 \|'
    
    new_content = re.sub(table_pattern, html_layout, current_content, flags=re.DOTALL)
    
    # Also we need to append the JS script tag at the end of the file if it's not there
    if '<script src="/js/armor-tooltip.js"></script>' not in new_content:
        new_content += '\n\n<script src="/js/armor-tooltip.js"></script>\n'
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully restored the 20:55 layout without the exploration text!")
else:
    print("Could not find HTML layout in a517bf9")
