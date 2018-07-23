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
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

import request



# Instantiate CvBridge
bridge = CvBridge()

def save_color_image_callback(msg):
    
    print("Received an image!")
    
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        
    except CvBridgeError, e:
        print(e)
        
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpeg', cv2_img)
        
        r = requests.get(cv2_img, allow_redirects=True)
        open('color-img.jpeg', 'wb').write(r.content)
        
        
def save_camera_info_callback(msg):
    
    print("camera info received!")
    
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "br8")
        
    except CvBridgeError, e: 
        print(e)
        
    else:
        cv2.imwrite('camera-info.jpeg', cv2_img)
        
        r = requests.get(cv2_img, allow_redirects=True)
        oppen('camera-info.jpeg', 'wb').write(r.content)
        
        

def save_image():
    rospy.init_node('image_listener')
    
    # Define your image topic
    image_topic_color_img = "/camera/depth/image_raw"
    image_topic_camera_info = "/camera/depth/camera_info"
    
    
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_color_img, Image, save_color_image_callback, queue_size=1)
    rospy.Subscriber(image_topic_camera_info, Image, save_camera_info_callback, queue_size=1)
    
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    save_image()