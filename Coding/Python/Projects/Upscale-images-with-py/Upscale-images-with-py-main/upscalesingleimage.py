import cv2

# Input image ka naam aur path
input_image_path = r"D:\UpscaleImg\image_35.jpg"  # r prefix ka istemal karke raw string ka istemal kiya hai

# Image ko load karna
input_image = cv2.imread(input_image_path)

# Upscaling factor
scale_factor = 2  # Yeh aapki choice ke according ho sakta hai

# Image ko upscale karna
upscaled_image = cv2.resize(input_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

# Upscaled image ko display karna
cv2.imshow('Upscaled Image', upscaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Upscaled image ko save karna
output_image_path = r"D:\UpscaleImg\upscaled_image.jpg"  # r prefix ka istemal karke raw string ka istemal kiya hai
cv2.imwrite(output_image_path, upscaled_image)
print("Upscaled image ko {} me save kiya gaya hai.".format(output_image_path))
