# Guide to run YOLOV2 on custom dataset

1. I followed these links to install and train YOLOV2 on custom dataset

https://pjreddie.com/darknet/yolo/
https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

1. I used LabelImg tool to annotate the images in PascalVoc format

https://github.com/tzutalin/labelImg

1. Modified the voc_label.py to convert my labels to yolov2 darknet format

1. Training the network with command and also created a log file for it

./darknet detector train cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23 | tee output.txt
