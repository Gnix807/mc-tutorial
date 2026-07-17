import os
import re

file_path = 'content/docs/ch01-getting-started/04-terminology.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First replace any downloaded /images/icons/... with the wiki url for processing
content = re.sub(r'<img src="/images/icons/([^"]+)"', r'<img src="https://zh.minecraft.wiki/images/\1"', content)

manual_mapping = {
    'EntitySprite_enderman.png': 'enderman_spawn_egg.png',
    'EntitySprite_creaking.png': 'creaking_spawn_egg.png',
    'EntitySprite_skeleton.png': 'skeleton_spawn_egg.png',
    'EntitySprite_warden.png': 'warden_spawn_egg.png',
    'EntitySprite_iron-golem.png': 'iron_golem_spawn_egg.png',
    'EntitySprite_zombified-piglin.png': 'zombified_piglin_spawn_egg.png',
    'EntitySprite_ghast.png': 'ghast_spawn_egg.png',
    'EntitySprite_zombie-pigman.png': 'zombified_piglin_spawn_egg.png',
    'EntitySprite_happy-ghast.png': 'ghast_spawn_egg.png',
    'EntitySprite_camel-husk.png': 'husk_spawn_egg.png',
    'EntitySprite_cave-spider.png': 'cave_spider_spawn_egg.png',
    'EntitySprite_leatherworker.png': 'villager_spawn_egg.png',
    'BiomeSprite_badlands.png': 'terracotta.png',
    'BiomeSprite_pale-garden.png': 'pale_oak_sapling.png',
    'EnvSprite_fortress.png': 'nether_bricks.png',
    'EnvSprite_bastion-remnant.png': 'polished_blackstone_bricks.png',
    'BlockSprite_carved-pumpkin.png': 'carved_pumpkin.png',
    'BlockSprite_hay-bale.png': 'hay_block_side.png',
    'BlockSprite_observer.png': 'observer_front.png',
    'BlockSprite_crafter.png': 'crafter_top.png',
    'ItemSprite_rotten-flesh.png': 'rotten_flesh.png'
}

def map_icon(url):
    filename = url.split('/')[-1]
    
    if filename in manual_mapping:
        local_name = manual_mapping[filename]
    else:
        # Default translation
        name = filename.split('_')[-1].replace('.png', '').replace('-', '_')
        if 'ItemSprite' in filename:
            local_name = f"{name}.png"
        elif 'BlockSprite' in filename:
            local_name = f"{name}.png"
        elif 'EntitySprite' in filename:
            local_name = f"{name}_spawn_egg.png"
        else:
            local_name = f"{name}.png"
            
    # Check if local file exists, otherwise fallback to a generic item (e.g. grass block)
    if not os.path.exists(f"static/images/items/{local_name}"):
        print(f"Warning: {local_name} not found! Falling back to dirt.")
        local_name = "dirt.png"
        
    return f'<img src="/images/items/{local_name}"'

new_content = re.sub(r'<img src="(https://zh\.minecraft\.wiki/images/[^"]+)"', lambda m: map_icon(m.group(1)), content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Mapped wiki urls to local items!")
