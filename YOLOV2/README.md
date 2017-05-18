# Guide to run YOLOV2 on custom dataset

1. I followed these links to install and train YOLOV2 on custom dataset

https://pjreddie.com/darknet/yolo/
https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

1. I used LabelImg tool to annotate the images in PascalVoc format

https://github.com/tzutalin/labelImg

1. Modified the voc_label.py to convert my labels to yolov2 darknet format

1. Training the network with command and also created a log file for it

`./darknet detector train cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23 | tee output.txt`

1. After training look at the avg loss and if it reaches a point where it doesn't decrease further stop the training.

1. It's also better to do cross validation, since the model might ovefit the data. To cross validate used the following command

`￼./darknet detector recall cfg/obj.data cfg/yolo-obj.cfg backup/yolo-obj_7000.weights`

**Note - Before this update the validation set details in the obj.data**

1. To to detection on an single image use the following command

`./darknet detector test cfg/obj.data cfg/yolo-obj.cfg backup/yolo-obj_7000.weights ../final_test/00f489dfe2b34a50c5fc4962749e11af.jpg`

**Note - The detections will be saved to the image called predictions.jpg and also the confidence will be shown in the promp**

1. To validate on the validation data which can be configured in the cfg/obj.data run the following command

`./darknet detector valid cfg/obj.data cfg/yolo-obj.cfg backup/yolo-obj_8000.weights -gpus 0`

** Note - The flag -gpus is required else we get a segmentation fault  and always use only single gpu for this purpose **

1. After validation the predictions will be stored in the results folder a single line as an example is illustrated below

*0aa270ece0509a3fda503bd76d4b5687 0.844032 383.764679 54.574635 396.045380 83.770981*

*Note - The first value is the name of the file, the second value is the confidence, the next ones are the cords of the bounding box*

