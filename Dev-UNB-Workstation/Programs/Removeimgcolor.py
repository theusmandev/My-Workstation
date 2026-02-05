# import cv2
# import numpy as np
# import os

# # Input folder ka path (yahan apna correct path daalein)
# input_folder = 'D:/New folder/Urdu Novel Bank/Images'

# # Output folder ka path input folder ke andar banayenge
# output_folder = os.path.join(input_folder, 'Processed_Images')

# # Ensure output folder exists
# if not os.path.exists(output_folder):
#     print(f"Output folder '{output_folder}' does not exist, creating it now...")
#     os.makedirs(output_folder)
# else:
#     print(f"Output folder '{output_folder}' already exists.")

# # Check if the input folder exists
# if not os.path.exists(input_folder):
#     print(f"Input folder '{input_folder}' not found. Exiting.")
# else:
#     print(f"Input folder '{input_folder}' found. Starting processing.")

# # Process each image
# for filename in os.listdir(input_folder):
#     # Only process files with specific extensions
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         # Image ka complete path
#         image_path = os.path.join(input_folder, filename)
#         print(f"Processing image: {image_path}")
        
#         # Image load karna
#         image = cv2.imread(image_path)
        
#         if image is not None:
#             # Red aur blue channels ko 0 karna
#             image[:, :, 0] = 0  # Blue channel (index 0)
#             image[:, :, 2] = 0  # Red channel (index 2)
            
#             # Output image ka path (processed folder ke andar save hoga)
#             output_path = os.path.join(output_folder, filename)
#             print(f"Saving processed image to: {output_path}")
#             # Image save karna
#             cv2.imwrite(output_path, image)
#         else:
#             print(f"Failed to load image: {image_path}")

# print("Tamam images successfully process ho chuki hain!")









# import cv2
# import numpy as np
# import os

# # Input folder ka path (apna correct path yahan dalain)
# input_folder = r"D:\New folder\inputimages"

# # Output folder ka path input folder ke andar banayenge
# output_folder = os.path.join(input_folder, 'Processed_Images')

# # Ensure output folder exists
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # Process each image
# for filename in os.listdir(input_folder):
#     # Only process files with specific extensions
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         # Image ka complete path
#         image_path = os.path.join(input_folder, filename)
#         # Image load karna
#         image = cv2.imread(image_path)
        
#         if image is not None:
#             # Red aur blue channels ko white (255) karna
#             image[:, :, 0] = 255  # Blue channel (index 0)
#             image[:, :, 2] = 255  # Red channel (index 2)
            
#             # Output image ka path (processed folder ke andar save hoga)
#             output_path = os.path.join(output_folder, filename)
#             # Image save karna
#             cv2.imwrite(output_path, image)

# print("Tamam images successfully process ho chuki hain, red aur blue colors ko white se replace kar diya gaya hai!")











import cv2
import numpy as np
import os

# Input folder ka path (apna correct path yahan dalain)
input_folder = r"C:\Users\Latitude\Downloads\ilovepdf_pages-to-jpg"

# Output folder ka path input folder ke andar banayenge
output_folder = os.path.join(input_folder, 'Processed_Images')

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to detect and change red and blue text to white
def replace_color_with_white(image):
    # Convert image to HSV (Hue, Saturation, Value) color space for better color detection
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for red
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # Define color range for blue
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create masks for red and blue
    mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Combine red masks
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Combine red and blue masks
    mask_combined = cv2.bitwise_or(mask_red, mask_blue)

    # Replace red and blue text with white color
    image[mask_combined > 0] = [255, 255, 255]

    return image

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Image ka complete path
        image_path = os.path.join(input_folder, filename)
        
        # Image load karna
        image = cv2.imread(image_path)
        
        if image is not None:
            # Call the function to replace red and blue text with white
            processed_image = replace_color_with_white(image)
            
            # Output image ka path (processed folder ke andar save hoga)
            output_path = os.path.join(output_folder, filename)
            
            # Image save karna
            cv2.imwrite(output_path, processed_image)

print("Tamam images successfully process ho chuki hain, sirf red aur blue text ko white se replace kiya gaya hai!")
