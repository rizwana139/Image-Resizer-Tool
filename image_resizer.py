import os
from PIL import Image

# Settings
input_folder = "input_images"      # Folder with original images
output_folder = "output_images"    # Folder to save resized images
target_size = (800, 600)           # Desired size (width, height)
output_format = "JPEG"             # Desired format: JPEG, PNG, etc.

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"]

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    name, ext = os.path.splitext(filename)
    if ext.lower() in valid_extensions:
        try:
            # Open the image
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Resize the image
            img_resized = img.resize(target_size)

            # Save the image
            output_path = os.path.join(output_folder, f"{name}.{output_format.lower()}")
            img_resized.save(output_path, output_format)

            print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
