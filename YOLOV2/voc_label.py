import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["red", "green"]


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(file_name):
    f_name = os.path.splitext(file_name)[0] # name of the file without extension
    print os.path.join(ann_dir,f_name+".xml")
    in_file = open(os.path.join(ann_dir,f_name+".xml"))
    out_file = open('labels/%s.txt'% f_name, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

data_dir = os.path.join(wd, "actual_data")
images_dir = os.path.join(data_dir, "images")
ann_dir = os.path.join(data_dir, "annotations")
os.makedirs('labels')

list_file = open('train.txt', 'w')
test_list = open('test.txt', 'w')
count  = 0

for f in os.listdir(images_dir):
    path_to_write = os.path.join(images_dir,f) #complete path of the file
    if count <= 550:
        list_file.write('%s\n'%path_to_write)
        count+=1
    else:
        test_list.write('%s\n'%path_to_write)
    convert_annotation(f)

list_file.close()

