import os
from PIL import Image

# ---------------- CONFIG ----------------
src_dir = r"C:\Users\koush\Downloads\dibeautypreneur_website_code\images_v2"
dst_dir = r"C:\Users\koush\Downloads\dibeautypreneur_website_code\images2_v2"

quality = 80  # 100 = lossless, <100 = lossy WebP quality
# ----------------------------------------

# Create target directory if it doesn't exist
os.makedirs(dst_dir, exist_ok=True)

for filename in os.listdir(src_dir):
    if filename.lower().endswith(".png"):
        src_path = os.path.join(src_dir, filename)
        dst_filename = os.path.splitext(filename)[0] + ".webp"
        dst_path = os.path.join(dst_dir, dst_filename)

        with Image.open(src_path) as img:
            if quality == 100:
                # Lossless
                img.save(dst_path, "WEBP", lossless=True)
            else:
                # Lossy with specified quality
                img.save(dst_path, "WEBP", quality=quality)

        print(f"Converted: {filename} -> {dst_filename} (quality={quality})")

print("Conversion completed.")
