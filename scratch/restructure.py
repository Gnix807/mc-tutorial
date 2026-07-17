import os
import re
import shutil

DOCS_DIR = 'content/docs'

def read_frontmatter(path):
    if not os.path.exists(path): return {}
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.match(r'^---\n(.*?)\n---(.*)', content, re.DOTALL)
    if not match: return {}
    
    fm_text = match.group(1)
    body = match.group(2)
    
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return {'fm': fm, 'body': body, 'raw': content}

def write_frontmatter(path, fm, body):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        for k, v in fm.items():
            f.write(f'{k}: {v}\n')
        f.write('---\n')
        f.write(body)

def process_chapter(chapter_dir, mapping):
    ch_path = os.path.join(DOCS_DIR, chapter_dir)
    if not os.path.exists(ch_path):
        os.makedirs(ch_path)

    temp_dir = os.path.join(ch_path, 'temp_reorg')
    os.makedirs(temp_dir, exist_ok=True)
    
    # mapping is a list of dicts: {'old_name': '...', 'new_name': '...', 'title': '...', 'weight': ...}
    for item in mapping:
        old_file = item.get('old_name')
        new_file = item['new_name']
        
        old_path = os.path.join(ch_path, old_file) if old_file else None
        new_path = os.path.join(temp_dir, new_file)
        
        if old_path and os.path.exists(old_path):
            data = read_frontmatter(old_path)
            fm = data.get('fm', {})
            body = data.get('body', '\n')
            fm['title'] = item['title']
            fm['weight'] = item['weight']
            write_frontmatter(new_path, fm, body)
        else:
            fm = {'title': item['title'], 'weight': item['weight'], 'type': 'docs'}
            body = '\n# ' + item['title'] + '\n\n（此处为占位内容，待后续完善）\n'
            write_frontmatter(new_path, fm, body)
            
    # move from temp back to chapter_dir
    # first, delete all existing .md files (except _index.md)
    for f in os.listdir(ch_path):
        if f.endswith('.md') and f != '_index.md' and f != 'temp_reorg':
            os.remove(os.path.join(ch_path, f))
            
    # copy from temp back
    for f in os.listdir(temp_dir):
        shutil.move(os.path.join(temp_dir, f), os.path.join(ch_path, f))
        
    os.rmdir(temp_dir)

# Special case for CH2: it had ch02-general which we need to migrate/delete
if os.path.exists(os.path.join(DOCS_DIR, 'ch02-general')):
    shutil.rmtree(os.path.join(DOCS_DIR, 'ch02-general'))
    
# CH1
ch1_mapping = [
    {'old_name': '01-buy-and-install.md', 'new_name': '01-buy-and-install.md', 'title': '购买与安装', 'weight': 1},
    {'old_name': '02-launcher-and-versions.md', 'new_name': '02-launcher-and-versions.md', 'title': '启动器与版本选择', 'weight': 2},
    {'old_name': '03-game-settings.md', 'new_name': '03-game-settings.md', 'title': '菜单与游戏设置', 'weight': 3},
    {'old_name': None, 'new_name': '04-terminology.md', 'title': '游戏术语与计量单位', 'weight': 4},
    {'old_name': None, 'new_name': '05-dos-and-donts.md', 'title': '新手不该做的事', 'weight': 5},
]
process_chapter('ch01-getting-started', ch1_mapping)

# CH2
ch2_mapping = [
    {'old_name': '01-first-day.md', 'new_name': '01-first-day.md', 'title': '生存第一天', 'weight': 1},
    {'old_name': None, 'new_name': '02-hunger-and-health.md', 'title': '饥饿与生命值管理', 'weight': 2},
    {'old_name': None, 'new_name': '03-shelter-basics.md', 'title': '庇护所选址与基础建造', 'weight': 3},
    {'old_name': '02-gathering-and-crafting.md', 'new_name': '04-gathering-and-crafting.md', 'title': '资源收集与合成', 'weight': 4},
    {'old_name': '03-mining.md', 'new_name': '05-mining.md', 'title': '采矿技术与洞穴探索', 'weight': 5},
    {'old_name': '03-combat-and-exploration.md', 'new_name': '06-combat-and-exploration.md', 'title': '战斗与外出探险', 'weight': 6},
    {'old_name': '04-farming.md', 'new_name': '07-farming.md', 'title': '基础农业与畜牧', 'weight': 7},
    {'old_name': '05-villagers.md', 'new_name': '08-villagers.md', 'title': '村庄机制与村民交易', 'weight': 8},
    {'old_name': '07-enchanting.md', 'new_name': '09-enchanting.md', 'title': '附魔与铁砧指南', 'weight': 9},
    {'old_name': '04-nether-and-end.md', 'new_name': '10-nether.md', 'title': '下界探险与快速旅行', 'weight': 10},
    {'old_name': None, 'new_name': '11-the-end.md', 'title': '完成冒险：击败末影龙', 'weight': 11},
]
process_chapter('ch02-survival', ch2_mapping)

# CH3
ch3_mapping = [
    {'old_name': '01-basics.md', 'new_name': '01-basics.md', 'title': '建筑术语与基础', 'weight': 1},
    {'old_name': '06-palette-and-materials.md', 'new_name': '02-palette-and-materials.md', 'title': '最佳建筑材料与调色', 'weight': 2},
    {'old_name': '02-styles.md', 'new_name': '03-styles.md', 'title': '房屋类型与建筑风格', 'weight': 3},
    {'old_name': '05-roofs-and-details.md', 'new_name': '04-roofs-and-details.md', 'title': '弧形屋顶与细节美化', 'weight': 4},
    {'old_name': '04-furniture.md', 'new_name': '05-furniture.md', 'title': '家具与内饰', 'weight': 5},
    {'old_name': '03-terraforming.md', 'new_name': '06-terraforming.md', 'title': '地形改造与自然景观', 'weight': 6},
    {'old_name': '07-underwater-and-special.md', 'new_name': '07-underwater-and-special.md', 'title': '水下建筑与特殊设计', 'weight': 7},
    {'old_name': None, 'new_name': '08-megaprojects.md', 'title': '巨型工程：大都市与过山车', 'weight': 8},
]
process_chapter('ch03-building', ch3_mapping)

# CH4
# Needs merging timers and clocks into logic circuits before processing
ch4_timers = os.path.join(DOCS_DIR, 'ch04-redstone/04-timers-and-clocks.md')
ch4_logic = os.path.join(DOCS_DIR, 'ch04-redstone/02-logic-circuits.md')
if os.path.exists(ch4_timers) and os.path.exists(ch4_logic):
    t_data = read_frontmatter(ch4_timers)
    l_data = read_frontmatter(ch4_logic)
    merged_body = l_data.get('body', '') + '\n\n' + t_data.get('body', '')
    write_frontmatter(ch4_logic, l_data.get('fm', {}), merged_body)
    os.remove(ch4_timers)

ch4_mapping = [
    {'old_name': '01-basics.md', 'new_name': '01-basics.md', 'title': '基础红石元件', 'weight': 1},
    {'old_name': '02-logic-circuits.md', 'new_name': '02-logic-circuits.md', 'title': '逻辑门与时钟电路', 'weight': 2},
    {'old_name': '05-piston-machines.md', 'new_name': '03-piston-machines.md', 'title': '活塞机械与隐藏门', 'weight': 3},
    {'old_name': None, 'new_name': '04-minecarts-and-transport.md', 'title': '矿车与物流系统', 'weight': 4},
    {'old_name': '06-storage-and-sorting.md', 'new_name': '05-storage-and-sorting.md', 'title': '物品分类与储存系统', 'weight': 5},
    {'old_name': '03-auto-farms.md', 'new_name': '06-auto-farms.md', 'title': '自动化农场与刷怪塔', 'weight': 6},
    {'old_name': None, 'new_name': '07-traps-and-defense.md', 'title': '陷阱与防御工程', 'weight': 7},
    {'old_name': '07-advanced-projects.md', 'new_name': '08-advanced-projects.md', 'title': '高级红石项目', 'weight': 8},
]
process_chapter('ch04-redstone', ch4_mapping)

# CH5
ch5_mapping = [
    {'old_name': '01-ways-to-connect.md', 'new_name': '01-ways-to-connect.md', 'title': '联机方式概述', 'weight': 1},
    {'old_name': '02-server-setup.md', 'new_name': '02-server-setup.md', 'title': '服务器搭建', 'weight': 2},
    {'old_name': '03-realms.md', 'new_name': '03-realms.md', 'title': 'Realms 领域', 'weight': 3},
    {'old_name': '04-server-management.md', 'new_name': '04-server-management.md', 'title': '服务器管理与指令', 'weight': 4},
    {'old_name': '05-pvp.md', 'new_name': '05-pvp.md', 'title': 'PvP 技巧与战术', 'weight': 5},
    {'old_name': None, 'new_name': '06-anti-griefing.md', 'title': '防破坏与权限管理', 'weight': 6},
]
process_chapter('ch05-multiplayer', ch5_mapping)

# CH6
ch6_mapping = [
    {'old_name': '01-mod-loaders.md', 'new_name': '01-mod-loaders.md', 'title': '模组加载器安装', 'weight': 1},
    {'old_name': '02-shaders-and-textures.md', 'new_name': '02-shaders-and-textures.md', 'title': '光影与资源包', 'weight': 2},
    {'old_name': '03-recommended-mods.md', 'new_name': '03-recommended-mods.md', 'title': '精品模组推荐', 'weight': 3},
    {'old_name': '04-optimization-and-qol.md', 'new_name': '04-optimization-and-qol.md', 'title': '性能优化与辅助功能', 'weight': 4},
    {'old_name': '05-modpacks.md', 'new_name': '05-modpacks.md', 'title': '整合包游玩指南', 'weight': 5},
    {'old_name': None, 'new_name': '06-bedrock-addons.md', 'title': '基岩版附加包 (Add-ons)', 'weight': 6},
]
process_chapter('ch06-mods', ch6_mapping)

# CH7
ch7_mapping = [
    {'old_name': '01-basic-commands.md', 'new_name': '01-basic-commands.md', 'title': '基础命令语法', 'weight': 1},
    {'old_name': '02-command-blocks.md', 'new_name': '02-command-blocks.md', 'title': '命令方块进阶', 'weight': 2},
    {'old_name': '03-datapacks.md', 'new_name': '03-datapacks.md', 'title': '数据包 (Data Packs)', 'weight': 3},
    {'old_name': '04-command-reference.md', 'new_name': '04-command-reference.md', 'title': '常用实用命令参考', 'weight': 4},
    {'old_name': '05-functions-and-advanced.md', 'new_name': '05-functions-and-advanced.md', 'title': '函数与高级应用', 'weight': 5},
    {'old_name': None, 'new_name': '06-map-making.md', 'title': '自定义地图制作与发布', 'weight': 6},
]
process_chapter('ch07-commands', ch7_mapping)

print("Restructuring completed successfully!")
