#!/usr/bin/env python

'''
Retrieved from: 
https://gist.github.com/rethink-imcmahon/77a1a4d5506258f3dc1f - 19/07/2018
''' 

'''
 Copyright (c) 2015, Rethink Robotics, Inc.

 Using this CvBridge Tutorial for converting
 ROS images to OpenCV2 images
 http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

 Using this OpenCV2 tutorial for saving Images:
 http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
'''

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image, CameraInfo
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

import numpy as np



# Instantiate CvBridge
bridge = CvBridge()
        
def save_camera_info_callback(msg):
    
    print("camera info received!")
    print(msg)
    
    try:
        camera_info = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt', 'w')
        msg_as_string = str(msg)
        camera_info.write(msg_as_string)
            
        camera_info.close()
        

    except CvBridgeError, e: 
        print(e)
        

def save_image():
    rospy.init_node('image_info_listener')
    
    # Define your image topic
    image_topic_camera_info = "/kinect_sim/camera1/rgb/camera_info"
    
    
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_camera_info, CameraInfo, save_camera_info_callback, queue_size=1)
    
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    save_image()