from PIL import Image, ImageFilter
from pathlib import Path
import os
os.makedirs("Gallagher_blur", exist_ok=True)

folder_path = Path("gallagher")
rasshireniya = (".png", ".jpg")
for file_path in folder_path.iterdir():
    file_rashirenie = file_path.suffix.lower()
    if file_rashirenie in rasshireniya:
        filename = "gallagher/" + file_path.name
        img = Image.open(filename)
        img_new = img.filter(ImageFilter.BLUR)
        new_filename = "Gallagher_blur/blured_" + file_path.name
        img_new.save(new_filename)


