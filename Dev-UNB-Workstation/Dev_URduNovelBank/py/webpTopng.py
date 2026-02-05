# import os
# from PIL import Image

# # Folder ka path jahan .webp files hain
# folder_path = r"D:\New folder\Urdu Novel Bank\Photopea done"

# # 'png' folder ka path
# png_folder_path = os.path.join(folder_path, 'png')

# # Agar 'png' folder nahi hai to bana dena
# if not os.path.exists(png_folder_path):
#     os.makedirs(png_folder_path)

# # Folder ke files per iterate karna
# for filename in os.listdir(folder_path):
#     if filename.endswith('.webp'):  # Corrected 'endswith'
#         webp_file_path = os.path.join(folder_path, filename)
#         png_file_name = filename.replace('.webp', '.png')
#         png_file_path = os.path.join(png_folder_path, png_file_name)

#         # WebP file ko kholna aur PNG me save karna
#         with Image.open(webp_file_path) as img:
#             img.save(png_file_path, 'PNG')

# print('Conversion Completed.')


import os
from PIL import Image

folder_path_webp = r"D:\New folder\Urdu Novel Bank\Photopea done"

png_folder_path = ''

for filename in os.listdir(folder_path_webp):
    if filename.endswith('.webp')