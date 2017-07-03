import os
import numpy as np

root = "/imagenet/2011/" 
val = "/imagenet/2011/bboxes/val/"

val_label = {}
gt_label = {}

def create_gt():
  count = 0
  with open('/imagenet/2011/train/labels.txt') as f:
    line = f.readlines()
  
  for i in range(len(line)):
    gt_label[line[i][0:-2]] = count
    count = count + 1
    
  f1 = open(os.path.join(root, "gtlabel.txt"), 'wb')
  for i in gt_label:
    f1.write(i + 't' + gt_label[i] + '\n')
  f1.close()
  
def create_train():



def create_val():





create_gt()
create_train()
create_val()






for (curr_dir, folder, files) in os.walk(val):
  for i in range(len(files)):
    filename = curr_dir + files[i]
    f2 = open(label,'r')
    for c in ( raw.strip().split() for raw in f2 ):
        gt_label.append() = c
        
    if filename.endwith('.xml') or filename.endwith('.XML'):
        f1 = open(filename,'r').read()
        
        
        start = f1.find('<name>')
        end = f1.find('</name>')
        
        img_label
