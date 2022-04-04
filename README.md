# Deep Sort in Realsense D435 
![](https://production-media.paperswithcode.com/thumbnails/task/task-0000000553-467cdf5d_SvoYQZ2.jpg)
## Install
clone from git repository 
```bash
$ git clone --recurse-submodules https://github.com/GiangNguyenMinh/DeepSort-Realsense-3D.git
```
Create environment
```bash
$ cd DeepSort-Realsense-3D
$ pip install -r requirements.txt
$ pip3 install pyrealsense2
```
## Tracking mode 
### Normal camera, webcam mode 
Reference README.md in repository [here](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch.git) with python track_realsence.py ...
### Realsense mode 
```bash
$ python track_realsence.py --realsence --show-vid
```
- Can select yolov5 version with argument --yolo_weights, and some setup arguments

