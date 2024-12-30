import sys
import os
from PIL import Image

if len(sys.argv) != 2:
    print("Usage: python crop_image.py <path>")
    print("'path' can be a file or a directory with multiple files")
    exit()

#Check if path is a file or a directory
isFile = None
argPath = sys.argv[1]
if os.path.isfile(argPath):
    isFile = bool(1)
elif os.path.isdir(argPath):
    isFile = bool(0)
else:
    print(f"Directory {argPath} doesn't exist")

def cropImage(filepath):
    try:
        with Image.open(filepath) as img:
            width, height = img.size
            mid_h = width // 2
            mid_v = height // 2
            
            if width >= height:
                width = height
            else:
                height = width
            
            box = (mid_h - (width // 2), mid_v - (height // 2), mid_h + (width // 2), mid_v + (height // 2))
            region = img.crop(box)
            path, ext = os.path.splitext(filepath)
            filename = path + "_cropped.jpg"
            region.save(filename, "JPEG")
    except IOError as err:
        print(err)

if isFile:
    cropImage(argPath)
else:
    for root, dirs, files in os.walk(argPath):
        # cropImage(file)
        print(f"Aktualny folder: {root}")
        print(f"Podfoldery: {dirs}")
        print(f"Pliki: {files}")
        for file in files:
            filepath = os.path.join(root, file)
            cropImage(filepath)