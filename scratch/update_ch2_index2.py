import re

filepath = 'content/_index.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_ch2_block = '''
-   [2.1 资源收集与合成]({{< relref "/docs/ch02-survival/01-gathering-and-crafting" >}})——资源采集、工具制作与合成系统
-   [2.2 饥饿与生命值管理]({{< relref "/docs/ch02-survival/02-hunger-and-health" >}})——保持生存的基础状态
-   [2.3 庇护所选址与基础建造]({{< relref "/docs/ch02-survival/03-shelter-basics" >}})——搭建你的第一个安全屋
-   [2.4 生存第一天]({{< relref "/docs/ch02-survival/04-first-day" >}})——从零开始的生存模式入门
-   [2.5 采矿技术与洞穴探索]({{< relref "/docs/ch02-survival/05-mining" >}})——高效挖矿技巧与矿石分布规律
-   [2.6 战斗与外出探险]({{< relref "/docs/ch02-survival/06-combat-and-exploration" >}})——战斗技巧、地图探索与结构寻宝
-   [2.7 基础农业与畜牧]({{< relref "/docs/ch02-survival/07-farming" >}})——农作物种植与动物养殖系统
-   [2.8 村庄机制与村民交易]({{< relref "/docs/ch02-survival/08-villagers" >}})——村民职业、交易系统与打折机制
-   [2.9 附魔与铁砧指南]({{< relref "/docs/ch02-survival/09-enchanting" >}})——附魔系统、经验获取与装备修复
-   [2.10 下界探险与快速旅行]({{< relref "/docs/ch02-survival/10-nether" >}})——下界维度的生存与交通
-   [2.11 完成冒险：击败末影龙]({{< relref "/docs/ch02-survival/11-the-end" >}})——进入末地，通关游戏
'''

pattern = r'(?<=### 第二章 · 生存指南\n\n).*?(?=\n### 第三章 · 建造美学)'
content = re.sub(pattern, new_ch2_block.strip(), content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index")
