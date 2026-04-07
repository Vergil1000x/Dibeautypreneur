import pillow_avif
import os
from PIL import Image

# ---------------- CONFIG ----------------
src_dir = r"C:\Users\koush\Downloads\dibeautypreneur_website_code\images_v3"
dst_dir = r"C:\Users\koush\Downloads\dibeautypreneur_website_code\images2_v3"

format_type = "avif"   # "webp" or "avif"
quality = 60           # 100 = lossless for WebP, for AVIF it's high quality
# ----------------------------------------

# Normalize format
format_type = format_type.lower()
if format_type not in ["webp", "avif"]:
    raise ValueError("format_type must be 'webp' or 'avif'")

# Create target directory if it doesn't exist
os.makedirs(dst_dir, exist_ok=True)

for filename in os.listdir(src_dir):
    if filename.lower().endswith(".png"):
        src_path = os.path.join(src_dir, filename)

        ext = ".webp" if format_type == "webp" else ".avif"
        dst_filename = os.path.splitext(filename)[0] + ext
        dst_path = os.path.join(dst_dir, dst_filename)

        with Image.open(src_path) as img:

            if format_type == "webp":
                if quality == 100:
                    img.save(dst_path, "WEBP", lossless=True)
                else:
                    img.save(dst_path, "WEBP", quality=quality)

            elif format_type == "avif":
                # AVIF save (requires Pillow with AVIF support)
                img.save(dst_path, "AVIF", quality=quality)

        print(f"Converted: {filename} -> {dst_filename} ({format_type}, quality={quality})")

print("Conversion completed.")