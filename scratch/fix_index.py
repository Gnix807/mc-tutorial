import re

filepath = 'content/_index.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '/docs/ch02-survival/02-gathering-and-crafting': '/docs/ch02-survival/04-gathering-and-crafting',
    '/docs/ch02-survival/03-mining': '/docs/ch02-survival/05-mining',
    '/docs/ch02-survival/04-farming': '/docs/ch02-survival/07-farming',
    '/docs/ch02-survival/05-villagers': '/docs/ch02-survival/08-villagers',
    '/docs/ch02-survival/03-combat-and-exploration': '/docs/ch02-survival/06-combat-and-exploration',
    '/docs/ch02-survival/07-enchanting': '/docs/ch02-survival/09-enchanting',
    '/docs/ch02-survival/04-nether-and-end': '/docs/ch02-survival/10-nether',
    '/docs/ch03-building/02-styles': '/docs/ch03-building/03-styles',
    '/docs/ch03-building/03-terraforming': '/docs/ch03-building/06-terraforming',
    '/docs/ch03-building/04-furniture': '/docs/ch03-building/05-furniture',
    '/docs/ch03-building/05-roofs-and-details': '/docs/ch03-building/04-roofs-and-details',
    '/docs/ch03-building/06-palette-and-materials': '/docs/ch03-building/02-palette-and-materials',
    '/docs/ch04-redstone/03-auto-farms': '/docs/ch04-redstone/06-auto-farms',
    '/docs/ch04-redstone/04-timers-and-clocks': '/docs/ch04-redstone/02-logic-circuits',
    '/docs/ch04-redstone/05-piston-machines': '/docs/ch04-redstone/03-piston-machines',
    '/docs/ch04-redstone/06-storage-and-sorting': '/docs/ch04-redstone/05-storage-and-sorting',
    '/docs/ch04-redstone/07-advanced-projects': '/docs/ch04-redstone/08-advanced-projects',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated links in content/_index.md")
