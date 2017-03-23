##Installation of SSD in caffe

Caffe was one of the troublemsome libraries required to be installed, since the training version of SSD was implemented 
only in Caffe during then (23.03.2017). Although there was a tensor flow implementation from author, it was prone to 
over-fitting and other problems, so decided to go ahead with the original caffe implementation. These are some important
points to take care of in case of a fresh install 

1. Make sure you setup the path's accurately (mainly for cuda, cudnn and anaconda paths) as shown in the below reference
https://github.com/tiangolo/caffe/blob/e12f3e4c565f68111bdbab396f7b256ac57de4f5/docs/install_apt2.md

1. Edit the Makefile.config based on how you want to configuration (backup of this file is available)

1. The list of commands are given in the original SSD installation instructions.
https://github.com/weiliu89/caffe/tree/ssd

1. During the command "make runtest -j8" I faced lots of errors when I was compiling with GPU support and in my case I 
had mulitple GPU's available. This one was really tricky and to overcome these errors I had to export two flags as
     1.`export MKL_CBWR=AUTO` # Makes sure that the results are deterministic in case of floating case numbers
     1.`export CUDA_VISIBLE_DEVICES=0` # Makes only one GPU visible

1. The .bashrc file, Makefile.config are backed up just in case.
