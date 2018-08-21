#!/usr/bin/env python

import rospy 
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
from smart_grasping_sandbox.smart_grasper import SmartGrasper
import time
from geometry_msgs.msg import Pose, Point
from tf.transformations import quaternion_from_euler
from math import pi, cos, sin

image_number = 0
bridge = CvBridge()

def save_color_image(msg):

# Retrieved from: 
# https://gist.github.com/rethink-imcmahon/77a1a4d5506258f3dc1f - 19/07/2018 :
    # Copyright (c) 2015, Rethink Robotics, Inc.
    # Using this CvBridge Tutorial for converting
    # ROS images to OpenCV2 images
    # http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

    # Using this OpenCV2 tutorial for saving Images:
    # http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

    
    rospy.loginfo("Recieved color image for dataset")
    
    try:
         
        # Convert your ROS Image message to OpenCV2
        color_img = bridge.imgmsg_to_cv2(msg, "bgr8")  # rgb image with red-/green-/blue-channel
        
        # Save your OpenCV2 image as a png 
        cv2.imwrite('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/color_image_' + str(image_number) + '.png', color_img)
       
    
    except CvBridgeError, e:
        print(e)
        

def save_depth_image(msg):
    
    rospy.loginfo("Recieved depth image for dataset")
    
    # cited code beginning
    # Retrieved from: https://answers.ros.org/question/255413/unable-to-store-the-depth-map-in-32fc1-format/ - 24/07/2018
    # Username: Joy16
    try:
        global image_number
        image_number += 1
        
        depth_img = bridge.imgmsg_to_cv2(msg,"passthrough")
        depth_array = np.array(depth_img, dtype=np.float32)
        cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)
        
        cv2.imwrite('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/depth_image_' + str(image_number) + '.png', depth_img)
     # cited code end  
     
    except CvBridgeError, er: 
        print(er)
        
def save_camera_info(msg):
    rospy.loginfo("Recieved camera info for dataset")
    
    camera_info = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/camera_info_' + str(image_number)+ '.txt', 'w')
    msg_as_string = str(msg)
    camera_info.write(msg_as_string)
            
    camera_info.close()

def gather_images():
    
    rospy.init_node('dataset_creator')
    
    # camera info topic
    image_topic_camera_info_img = "/kinect_sim/camera1/rgb/camera_info"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_camera_info_img, CameraInfo, save_camera_info, queue_size=1)
    
    # color image topic
    image_topic_color_img = "/kinect_sim/camera1/rgb/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_color_img, Image, save_color_image, queue_size=1)
    
    # depth image topic
    image_topic_depth_img = "/kinect_sim/camera1/depth/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_depth_img, Image, save_depth_image, queue_size=1)
    
     # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    gather_images()
