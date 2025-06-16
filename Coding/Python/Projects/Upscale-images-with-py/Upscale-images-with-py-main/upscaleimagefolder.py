import os
import cv2

# Input folder ka path jismein 1000 images hain
input_folder_path = r"D:\UpscaleImg\Input_images"

# Output folder ka path jismein upscaled images save ki jayengi
output_folder_path = r"D:\UpscaleImg\Output_images"
os.makedirs(output_folder_path, exist_ok=True)

# Upscaling factor
scale_factor = 2  # Yeh aapki choice ke according ho sakta hai

# Loop through har ek image ko upscale karne ke liye
for filename in os.listdir(input_folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Sirf image files ko consider karein
        input_image_path = os.path.join(input_folder_path, filename)
        input_image = cv2.imread(input_image_path)
        
        # Image ko upscale karna
        upscaled_image = cv2.resize(input_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
        
        # Upscaled image ko save karna
        output_image_path = os.path.join(output_folder_path, filename)
        cv2.imwrite(output_image_path, upscaled_image)
        print("Upscaled image ko {} me save kiya gaya hai.".format(output_image_path))
