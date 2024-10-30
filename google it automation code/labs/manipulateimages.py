#!/usr/bin/env python3

#import modules

from PIL import Image
import os

#define directories

directory = "images/"
outputdirectory = "/opt/icons/"

#construct loop: for the filenames in the directory, if image files, open with the complete pathname, rotate, resize, convert to rgb, save in new directory using comlete pathname and extension 

for filename in os.listdir(directory):
  if filename != ".DS_Store":
    thing = Image.open(os.path.join(directory, filename))
    thing = thing.rotate(-90)
    thing = thing.resize((128,128))
    thing = thing.convert("RGB")
    thing.save(os.path.join(outputdirectory, filename+".jpeg"))
    
    
    
    