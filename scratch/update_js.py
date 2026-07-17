import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where img.src is set
    # insert onload handler before it
    new_code = '''
        img.onload = function() {
          if (this.naturalWidth >= 256) {
            this.style.setProperty("image-rendering", "auto", "important");
          } else {
            this.style.setProperty("image-rendering", "pixelated", "important");
          }
        };
        img.src = "/images/items/" + itemKey + ".png";'''
        
    content = content.replace('img.src = "/images/items/" + itemKey + ".png";', new_code)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('layouts/shortcodes/crafting.html')
update_file('layouts/shortcodes/smithing.html')
