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


# Instantiate CvBridge
bridge = CvBridge()

def save_color_image_callback(msg):
    
    print("Received a color image!")
    
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")  # rgb image with red-/green-/blue-channel
        
        # Save your OpenCV2 image as a png 
        cv2.imwrite('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs/camera_image.png', cv2_img)
        
    except CvBridgeError, e:
        print(e)
        
        
def save_image():
    rospy.init_node('image_listener')
    
    # Define your image topic
    image_topic_color_img = "/kinect_sim/camera1/rgb/image_raw"
    
    
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_color_img, Image, save_color_image_callback, queue_size=1)

    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    save_image()