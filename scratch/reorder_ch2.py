import os

ch2_dir = 'content/docs/ch02-survival'

# Current files:
# 01-first-day.md (生存第一天)
# 02-hunger-and-health.md (饥饿与生命值)
# 03-shelter-basics.md (庇护所)
# 04-gathering-and-crafting.md (资源收集)

# Target order:
# 1. 资源收集与合成
# 2. 饥饿与生命值
# 3. 庇护所
# 4. 生存第一天

moves = [
    ('04-gathering-and-crafting.md', '01-gathering-and-crafting.md', '1'),
    ('02-hunger-and-health.md', '02-hunger-and-health_tmp.md', '2'), # temp to avoid clash
    ('03-shelter-basics.md', '03-shelter-basics_tmp.md', '3'),
    ('01-first-day.md', '04-first-day.md', '4')
]

for old, new, weight in moves:
    old_path = os.path.join(ch2_dir, old)
    new_path = os.path.join(ch2_dir, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        
        # update weight
        with open(new_path, 'r', encoding='utf-8') as f:
            content = f.read()
        import re
        content = re.sub(r'^weight: \d+', f'weight: {weight}', content, flags=re.MULTILINE)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Fix tmp names
os.rename(os.path.join(ch2_dir, '02-hunger-and-health_tmp.md'), os.path.join(ch2_dir, '02-hunger-and-health.md'))
os.rename(os.path.join(ch2_dir, '03-shelter-basics_tmp.md'), os.path.join(ch2_dir, '03-shelter-basics.md'))
print("Reordered successfully!")
