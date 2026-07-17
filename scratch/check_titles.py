import os
for root, dirs, files in os.walk('content/docs'):
    for f in files:
        if f.endswith('.md'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines[:10]:
                    if line.startswith('title:'):
                        print(f"{f}: {line.strip()}")
