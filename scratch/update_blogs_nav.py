import os
import re

def update_nav():
    # Update files in pages/
    pages_dir = 'pages'
    for f in os.listdir(pages_dir):
        if f.endswith('.html'):
            path = os.path.join(pages_dir, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Look for Gallery link and insert Blogs after it
            target = '<li class="nav-item"><a class="nav-link" href="projects.html">Gallery</a></li>'
            replacement = target + '\n                                <li class="nav-item"><a class="nav-link" href="../blogs/index.html">Blogs</a></li>'
            
            if target in content and '../blogs/index.html' not in content:
                new_content = content.replace(target, replacement)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {path}")

    # Also update footer links if applicable
    # (Optional, but good for consistency)
    for f in os.listdir(pages_dir):
        if f.endswith('.html'):
            path = os.path.join(pages_dir, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Update footer links
            footer_target = '<li><a href="projects.html">Gallery</a></li>'
            footer_replacement = footer_target + '\n                            <li><a href="../blogs/index.html">Blogs</a></li>'
            
            if footer_target in content and '../blogs/index.html' not in content:
                new_content = content.replace(footer_target, footer_replacement)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated footer in {path}")

if __name__ == "__main__":
    update_nav()
