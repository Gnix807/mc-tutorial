import os
import re

content_dir = 'content/docs'
index_file = 'content/_index.md'

sections = []

# Get all ch* directories
ch_dirs = sorted([d for d in os.listdir(content_dir) if d.startswith('ch') and os.path.isdir(os.path.join(content_dir, d))])

for ch_dir in ch_dirs:
    idx_path = os.path.join(content_dir, ch_dir, '_index.md')
    if not os.path.exists(idx_path): continue
    
    with open(idx_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    title_match = re.search(r'title:\s*(.*)', idx_content)
    ch_title = title_match.group(1).strip() if title_match else ch_dir
    
    sections.append(f'### {ch_title}\n')
    
    # Get all .md files in the directory except _index.md
    md_files = sorted([f for f in os.listdir(os.path.join(content_dir, ch_dir)) if f.endswith('.md') and f != '_index.md'])
    
    for md_file in md_files:
        md_path = os.path.join(content_dir, ch_dir, md_file)
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        title_match = re.search(r'title:\s*(.*)', md_content)
        file_title = title_match.group(1).strip() if title_match else md_file.replace('.md', '')
        
        # Remove weight if present in title like "1.1 xxx"
        
        relref_path = f'/docs/{ch_dir}/{md_file.replace(".md", "")}'
        sections.append(f'-   [{file_title}]({{{{< relref "{relref_path}" >}}}}) —— (待补充简介)')
    
    sections.append('')

new_index = f'''---
title: Minecraft 从入门到精通
type: docs
---

# Minecraft 从入门到精通

欢迎阅读这份 Minecraft 教程！这是一份面向 MC 新手的图文教程，从零开始带你逐步掌握这款游戏的核心玩法与进阶技巧。

无论你是刚接触 Minecraft 的萌新，还是想补全知识盲区的老玩家，这里都有适合你的内容。零门槛、有深度、重实战——让我们一起来探索这个方块组成的无限世界。

---

## 目录

本文档内容按照由浅入深的顺序编排，建议按章节顺序阅读。

-   [**序**]({{{{< relref "/docs/preamble" >}}}})——关于这份教程的由来与使用建议

{chr(10).join(sections)}

-   [**附录**]({{{{< relref "/docs/appendix" >}}}})——常用工具与参考链接
-   [**后记**]({{{{< relref "/docs/afterwords" >}}}})

---

## 反馈与交流

如果您对本教程有任何意见或建议，欢迎通过以下方式联系：

-   在 [GitHub 仓库](https://github.com/Gnix807/mc-tutorial) 提交 Issue
-   发送邮件到教程维护邮箱

---

## 许可与声明

本教程所有原创内容以 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 协议授权。您可以自由分享、复制本教程内容及基于此进行二次创作，但须注明原作者与出处，且不得用于商业用途。

本教程中出现的 Minecraft 相关商标与游戏素材归 Mojang Studios / Microsoft 所有。引用仅用于教学与介绍目的。
'''

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(new_index)

print("Generated new _index.md")
