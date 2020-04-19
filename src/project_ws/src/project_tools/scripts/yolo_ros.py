import argparse
from sys import platform

from models import *  # set ONNX_EXPORT in models.py
from utils.datasets import *
from utils.utils import *

import rospy
from project_tools.msg import Ndarray_image
import numpy as np
import cv2

class yolo_converter:
    def __init__(self):
        rospy.Subscriber("image_array", Ndarray_image, self.callback)
        self.loading()

    def loading(self, save_txt=False, save_img=False, stream_img=False):
        print (opt)
        print('detect called')
        self.img_size = (320, 192) if ONNX_EXPORT else opt.img_size  # (320, 192) or (416, 256) or (608, 352) for (height, width)
        self.out, weights, self.half = opt.output, opt.weights, opt.half

        # Initialize
        self.device = torch_utils.select_device(device='cpu' if ONNX_EXPORT else opt.device)
        if os.path.exists(self.out):
            shutil.rmtree(self.out)  # delete output folder
        os.makedirs(self.out)  # make new output folder
        print(self.out)
        # Initialize model
        self.model = Darknet(opt.cfg, self.img_size)
        print(weights)
        # Load weights
        if weights.endswith('.pt'):  # pytorch format
            self.model.load_state_dict(torch.load(weights, map_location=self.device)['model'])
        else:  # darknet format
            _ = load_darknet_weights(model, weights)
        print('model loaded')
        # Fuse Conv2d + BatchNorm2d layers
        # model.fuse()

        # Eval mode
        self.model.to(self.device).eval()

        # Export mode
        if ONNX_EXPORT:
            img = torch.zeros((1, 3) + self.img_size)  # (1, 3, 320, 192)
            torch.onnx.export(self.model, img, 'weights/export.onnx', verbose=True)
            return

        # Half precision
        self.half = self.half and self.device.type != 'cpu'  # half precision only supported on CUDA
        if self.half:
            self.model.half()

        # Set Dataloader
        vid_path, vid_writer = None, None

        # Get classes and colors
        print(parse_data_cfg(opt.data)['names'])
        self.classes = load_classes(parse_data_cfg(opt.data)['names'])
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(self.classes))]




    def callback(self, data):
        ndarray_image = np.array(data.data, dtype=np.uint8).reshape((data.dimension[0], data.dimension[1], data.dimension[2]))

        img0 = ndarray_image
        img0 = cv2.flip(img0, 1)  # flip left-right
        img_path = 'webcam.jpg'
        # print('webcam %g: ' % self.count, end='')

        # Padded resize
        img, *_ = letterbox(img0, new_shape=self.img_size)

        # Normalize RGB
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB
        img = np.ascontiguousarray(img, dtype=np.float16 if self.half else np.float32)  # uint8 to fp16/fp32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0

        path = img_path
        im0s = img0

        # Run inference
        # for path, img, im0s, vid_cap in dataset:
        t = time.time()

        # Get detections
        # print ("----------------------------")
        img = torch.from_numpy(img).to(self.device)
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        pred, _ = self.model(img)

        for i, det in enumerate(non_max_suppression(pred, opt.conf_thres, opt.nms_thres)):  # detections per image
            p, s, im0 = path, '', im0s

            save_path = str(Path(self.out) / Path(p).name)
            s += '%gx%g ' % img.shape[2:]  # print string
            if det is not None and len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    # print(int(c)) 
                    # print(self.classes)
                    s += '%g %ss, ' % (n, self.classes[int(c)])  # add to string

                # Write results
                for *xyxy, conf, _, cls in det:
                    # print (xyxy)
                    # print (type(xyxy[0].item()))
                    # print (xyxy[0].item())
                    label = '%s %.2f' % (self.classes[int(cls)], conf)
                    plot_one_box(xyxy, im0, label=label, color=self.colors[int(cls)])

            # print('%sDone. (%.3fs)' % (s, time.time() - t))
            # print(save_path)

            # Stream results
            cv2.imshow(p, im0)
        
        cv2.waitKey(3)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default='cfg/yolov3-spp.cfg', help='cfg file path')
    parser.add_argument('--data', type=str, default='data/coco.data', help='coco.data file path')
    parser.add_argument('--weights', type=str, default='weights/yolov3-spp.weights', help='path to weights file')
    parser.add_argument('--source', type=str, default='data/samples', help='source')  # input file/folder, 0 for webcam
    parser.add_argument('--output', type=str, default='output', help='output folder')  # output folder
    parser.add_argument('--img-size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.3, help='object confidence threshold')
    parser.add_argument('--nms-thres', type=float, default=0.5, help='iou threshold for non-maximum suppression')
    parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
    parser.add_argument('--half', action='store_true', help='half precision FP16 inference')
    parser.add_argument('--device', default='', help='device id (i.e. 0 or 0,1) or cpu')
    opt = parser.parse_args()
    """
    opt.cfg = "/content/drive/My Drive/TrainingYoloV3/" + opt.cfg
    opt.data = "/content/drive/My Drive/TrainingYoloV3/" + opt.data
    opt.weights = "/content/drive/My Drive/TrainingYoloV3/" + opt.weights
    opt.source = "/content/drive/My Drive/TrainingYoloV3/" + opt.source
    opt.output = "/content/drive/My Drive/TrainingYoloV3/" + opt.output

    """

    yc = yolo_converter()
    rospy.init_node('image_detect', anonymous=True)

    rospy.spin()
