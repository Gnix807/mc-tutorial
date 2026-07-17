import os
import re
import urllib.request
import time

file_path = 'content/docs/ch01-getting-started/04-terminology.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I changed it to <img src="/images/icons/..." in the previous script!
# Wait, I need to restore the URLs first if they were changed but download failed.
# Let's see if the markdown has /images/icons
