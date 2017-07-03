import os
import numpy as np

root = "/imagenet/2011/" 
val = "/imagenet/2011/bboxes/val/"

val_label = {}
gt_label = {}

def create_gt():
  f = open(root + 'train/labels.txt', 'r')
  c = 0
  for c in ( raw.strip().split() for raw in f):
    gt_label[c[0]]  = c
    c+=1
  
  f.close()
  f = open(os.path.join(root, "gtlabel.txt"), 'wb')
  for i in gt_label:
    f.write(i + '\n')
  f.close()
  
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
