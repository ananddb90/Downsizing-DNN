
import os
import numpy as np

root = '/imagenet/2011/'
img_label = {}
val = []

for (par_curpath, par_dirnam, par_filnam) in os.walk(os.path.join(root, 'train')):
       for i in range(len(par_dirnam)):
               for (child_curpath, child_dirnam, child_filnam) in os.walk(root + 'train/' + par_dirnam[i]):
                       for j in range(len(child_filnam)):
                               img_label[par_dirnam[i] + '/' + child_filnam[j]] = i



f = open(os.path.join(root, 'train.txt'),'wb')
for i in img_label:
       f.write(i + '\t' + str(img_label[i]) + '\n')

f.close()



#with open('/rfcn/py-R-FCN/caffe/data/ilsvrc12/val.txt') as file:
#       filedata = file.read()

f = open('/rfcn/py-R-FCN/caffe/data/ilsvrc12/val.txt').xreadlines()

for l in f:
        new = l.replace('ILSVRC2012_', 'ILSVRC2011_')
        val.append(new)

f2 = open(os.path.join(root, 'val.txt'), 'wb')
for i in val:
        f2.write(i)
f2.close()
f.close()


