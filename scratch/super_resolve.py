import os
import pygame
from PIL import Image

pygame.init()
pygame.display.set_mode((1, 1), pygame.HIDDEN)

directory = 'static/images/items/'
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        filepath = os.path.join(directory, filename)
        
        # Open with PIL to check size
        img_pil = Image.open(filepath).convert("RGBA")
        if img_pil.size == (32, 32):
            # Load with pygame
            surf = pygame.image.load(filepath)
            
            # Apply scale2x twice to get 128x128
            surf_2x = pygame.transform.scale2x(surf)
            surf_4x = pygame.transform.scale2x(surf_2x)
            
            # Save temporary 128x128
            temp_path = filepath + '.temp.png'
            pygame.image.save(surf_4x, temp_path)
            
            # Open 128x128 with PIL and downscale to 96x96 using Lanczos
            img_128 = Image.open(temp_path).convert("RGBA")
            img_96 = img_128.resize((96, 96), Image.Resampling.LANCZOS)
            
            # Overwrite original with 96x96 super-resolved version
            img_96.save(filepath)
            os.remove(temp_path)
            print(f"Super-resolved: {filename}")
