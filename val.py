import os
import numpy as np

val = "/imagenet/2011/bboxes/val/"
label = "/imagenet/2011/imagenet.txt"

img_label = {}

for (curr_dir, folder, files) in os.walk(val):
  for i in range(files):
    img_id = 
