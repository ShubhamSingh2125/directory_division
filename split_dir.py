# directory_division
import os
import random
import shutil

# Paths
source_dir = r"C:\Users\KIIT0001\Desktop\PM\root\sorted_folder" # Folder with all images
target_dir = r"C:\Users\KIIT0001\Desktop\PM\root\Main_project"    # Where the YOLO structure will be created

# Train/val split ratio
train_ratio = 0.8

# Create directories
os.makedirs(os.path.join(target_dir, "images/train"), exist_ok=True)
os.makedirs(os.path.join(target_dir, "images/val"), exist_ok=True)
os.makedirs(os.path.join(target_dir, "labels/train"), exist_ok=True)
os.makedirs(os.path.join(target_dir, "labels/val"), exist_ok=True)

# Get all image files (change extensions if needed)
image_extensions = [".jpg", ".jpeg", ".png"]
images = [f for f in os.listdir(source_dir) if os.path.splitext(f)[1].lower() in image_extensions]

# Shuffle and split
random.shuffle(images)
split_idx = int(len(images) * train_ratio)
train_images = images[:split_idx]
val_images = images[split_idx:]

# Copy images to respective folders
for img in train_images:
    shutil.copy(os.path.join(source_dir, img), os.path.join(target_dir, "images/train", img))

for img in val_images:
    shutil.copy(os.path.join(source_dir, img), os.path.join(target_dir, "images/val", img))

print(f"Split complete! {len(train_images)} training and {len(val_images)} validation images created.")
