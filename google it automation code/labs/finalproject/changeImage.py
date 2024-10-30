#!/usr/bin/env python3
from PIL import Image
import os

location = "./supplier-data/images/"
for file in os.listdir("./supplier-data/images"):
    if file.endswith(".tiff"):
        splitfilename = file.split(".")
        filename = splitfilename[0] + ".jpeg"
        im = Image.open(location + file).convert("RGB")
        im.resize((600, 400)).save("./supplier-data/images/" + filename, "JPEG")
        
#simple data manipulation stuff, this should work


        
        
        
        
    
