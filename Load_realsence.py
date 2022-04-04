import cv2
import time

from yolov5.utils.augmentations import letterbox
from yolov5.utils.general import LOGGER
import numpy as np
from threading import Thread
from realsense_depth import*


class LoadRealsence:
    # YOLOv5 local webcam dataloader, i.e. `python detect.py --source 0`
    def __init__(self, img_size=640, stride=32):
        self.img_size = img_size
        self.stride = stride

        self.dc = DepthCamera() # read realsence
        # self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # set buffer size

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if cv2.waitKey(1) == ord('q'):  # q to quit
            self.dc.release()
            cv2.destroyAllWindows()
            raise StopIteration

        # Read frame
        ret_val, dept_frame, img0 = self.dc.get_frame()
        img0 = [cv2.flip(img0, 1)]  # flip left-right

        # Print
        assert ret_val, f'Camera Error camera'
        img_path = 'realsence.jpg'
        s = f'realsence {self.count}: '

        # Padded resize
        img = np.array([letterbox(img0[0], self.img_size, stride=self.stride)[0]])

        # Convert
        # img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        # img = np.ascontiguousarray(img)

        img = img[..., ::-1].transpose((0, 3, 1, 2))  # BGR to RGB, BHWC to BCHW
        img = np.ascontiguousarray(img)

        return img_path, img, img0, None, s, [dept_frame]

    def __len__(self):
        return 0