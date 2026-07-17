import re

filepath = r'c:\Users\Gnix807\Desktop\新建文件夹\MC教程\content\docs\ch02-general\01-combat-and-exploration.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

armor_data = {
    "leather_helmet_default": ("皮革帽子", "护甲值: +1"),
    "leather_chestplate_default": ("皮革外套", "护甲值: +3"),
    "leather_leggings_default": ("皮革裤子", "护甲值: +2"),
    "leather_boots_default": ("皮革靴子", "护甲值: +1"),
    
    "iron_helmet": ("铁头盔", "护甲值: +2"),
    "iron_chestplate": ("铁胸甲", "护甲值: +6"),
    "iron_leggings": ("铁护腿", "护甲值: +5"),
    "iron_boots": ("铁靴子", "护甲值: +2"),
    
    "diamond_helmet": ("钻石头盔", "护甲值: +3 | 盔甲韧性: +2"),
    "diamond_chestplate": ("钻石胸甲", "护甲值: +8 | 盔甲韧性: +2"),
    "diamond_leggings": ("钻石护腿", "护甲值: +6 | 盔甲韧性: +2"),
    "diamond_boots": ("钻石靴子", "护甲值: +3 | 盔甲韧性: +2"),
    
    "netherite_helmet": ("下界合金头盔", "护甲值: +3 | 盔甲韧性: +3 | 击退抗性: +1"),
    "netherite_chestplate": ("下界合金胸甲", "护甲值: +8 | 盔甲韧性: +3 | 击退抗性: +1"),
    "netherite_leggings": ("下界合金护腿", "护甲值: +6 | 盔甲韧性: +3 | 击退抗性: +1"),
    "netherite_boots": ("下界合金靴子", "护甲值: +3 | 盔甲韧性: +3 | 击退抗性: +1"),
    
    "turtle_helmet": ("海龟壳", "护甲值: +2 | 赋予水下呼吸效果")
}

def repl(match):
    full_match = match.group(0)
    slot_tag = match.group(1)
    img_tag = match.group(2)
    img_src = match.group(3)
    
    filename = img_src.split('/')[-1].replace('.png', '')
    
    if filename in armor_data:
        title, subtitle = armor_data[filename]
        # Insert data attributes into the slot div
        new_slot_tag = slot_tag.replace('class="mc-crafting-slot"', f'class="mc-crafting-slot" data-tooltip-title="{title}" data-tooltip-subtitle="{subtitle}"')
        return f"{new_slot_tag}{img_tag}"
    return full_match

# Match `<div class="mc-crafting-slot"><img src="..." /></div>`
# Note that we use a broader regex for the slot wrapper since the turtle shell is a span
new_content = re.sub(r'(<(?:div|span)[^>]*?class="mc-crafting-slot"[^>]*?>)(<img[^>]*?src="([^"]+)"[^>]*?>)', repl, content)

script = """
<script>
document.addEventListener("DOMContentLoaded", () => {
  let tooltip = document.querySelector(".mc-crafting-tooltip");
  if (!tooltip) {
    tooltip = document.createElement("div");
    tooltip.className = "mc-crafting-tooltip";
    tooltip.innerHTML = '<span class="mc-tooltip-title"></span><span class="mc-tooltip-subtitle"></span>';
    document.body.appendChild(tooltip);
  }

  const customSlots = document.querySelectorAll('.mc-crafting-slot[data-tooltip-title]');
  customSlots.forEach(slot => {
    slot.addEventListener("mouseenter", (e) => {
      tooltip.querySelector(".mc-tooltip-title").textContent = slot.getAttribute("data-tooltip-title");
      tooltip.querySelector(".mc-tooltip-subtitle").textContent = slot.getAttribute("data-tooltip-subtitle");
      tooltip.style.display = "block";
    });

    slot.addEventListener("mousemove", (e) => {
      tooltip.style.left = (e.clientX + 12) + "px";
      tooltip.style.top = (e.clientY - 12) + "px";
    });

    slot.addEventListener("mouseleave", () => {
      tooltip.style.display = "none";
    });
  });
});
</script>
"""

# Only append script if not already present
if 'document.querySelectorAll(\'.mc-crafting-slot[data-tooltip-title]\')' not in new_content:
    new_content += script

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Tooltips added!")
