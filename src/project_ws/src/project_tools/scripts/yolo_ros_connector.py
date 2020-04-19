#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from project_tools.msg import Ndarray_image
from cv_bridge import CvBridge, CvBridgeError

import numpy


class image_converter:

    def __init__(self):
        self.pub = rospy.Publisher('image_array', Ndarray_image, queue_size=10)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("camera/rgb/image_raw", Image, self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        image_array = Ndarray_image()
        image_array.data = cv_image.flatten()
        image_array.dimension = [len(cv_image), len(cv_image[0]), len(cv_image[0][0])]
        self.pub.publish(image_array)


def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
