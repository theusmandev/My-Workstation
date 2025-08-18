# import os
# import xml.etree.ElementTree as ET
# from datetime import datetime
# import re

# # Paths
# XML_FILE = 'blog-07-2025.xml'
# OUTPUT_DIR = 'output_html'

# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # Blogger XML uses Atom format
# ns = {'atom': 'http://www.w3.org/2005/Atom'}

# # Helper to create safe filenames
# def slugify(text):
#     text = text.lower()
#     text = re.sub(r'\W+', '-', text)
#     return text.strip('-')

# # Parse XML
# tree = ET.parse(XML_FILE)
# root = tree.getroot()

# for entry in root.findall('atom:entry', ns):
#     if entry.find('atom:category', ns) is not None:
#         title = entry.find('atom:title', ns).text or "Untitled"
#         content = entry.find('atom:content', ns).text or ""
#         published = entry.find('atom:published', ns).text
#         date_obj = datetime.strptime(published[:10], "%Y-%m-%d")

#         slug = slugify(title)
#         filename = f"{slug}.html"
#         filepath = os.path.join(OUTPUT_DIR, filename)

#         # Simple HTML structure
#         html = f"""<!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>{title}</title>
# </head>
# <body>
#     <h1>{title}</h1>
#     <p><em>{date_obj.strftime('%B %d, %Y')}</em></p>
#     <div>{content}</div>
# </body>
# </html>
# """

#         # Save the HTML file
#         with open(filepath, 'w', encoding='utf-8') as f:
#             f.write(html)

# print("✅ All posts converted to static HTML in 'output_html/' folder.")









import os
import xml.etree.ElementTree as ET
from datetime import datetime
import re

# Paths
XML_FILE = r""
OUTPUT_DIR = r""

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Blogger XML uses Atom format
ns = {'atom': 'http://www.w3.org/2005/Atom'}

# Helper to create safe filenames
def slugify(text):
    text = text.lower()
    text = re.sub(r'\W+', '-', text)
    return text.strip('-')

# Parse XML
tree = ET.parse(XML_FILE)
root = tree.getroot()

for entry in root.findall('atom:entry', ns):
    if entry.find('atom:category', ns) is not None:
        title = entry.find('atom:title', ns).text or "Untitled"
        content = entry.find('atom:content', ns).text or ""
        published = entry.find('atom:published', ns).text
        date_obj = datetime.strptime(published[:10], "%Y-%m-%d")

        slug = slugify(title)
        filename = f"{slug}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Simple HTML structure
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p><em>{date_obj.strftime('%B %d, %Y')}</em></p>
    <div>{content}</div>
</body>
</html>
"""

        # Save the HTML file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("✅ All posts converted to static HTML in 'output_html/' folder.")
