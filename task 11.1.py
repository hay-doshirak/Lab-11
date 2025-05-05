from PIL import Image, ImageFilter
import os
os.makedirs("gallagher_no", exist_ok=True)
for i in range(1,6):
    filename="gallagher/G"+ str(i)+".jpg"
    img = Image.open(filename)
    img_new = img.filter(ImageFilter.CONTOUR)
    new_filename="gallagher_no/g"+str(i)+".jpg"
    img_new.save(new_filename)
