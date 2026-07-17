from PIL import Image

img = Image.open('static/images/items/oak_planks.png').convert("RGBA")
bbox = img.getbbox()
# bbox is (4, 2, 28, 32) -> width 24, height 30
cropped = img.crop(bbox)

# Squish height from 30 to 24 to make it 1:1 aspect ratio like in-game!
squished = cropped.resize((24, 24), Image.Resampling.LANCZOS)

# Create a new 32x32 transparent image and paste it in the center
new_img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
new_img.paste(squished, (4, 4)) # (32-24)/2 = 4

new_img.save('scratch/squished_oak.png')
