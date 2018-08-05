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

bridge = CvBridge()
image_number = 0

def move_robot_around_object(pose):
    grasper = SmartGrasper()
    
    pose.position.x += 0.3
    pose.position.y += 0.1
    pose.position.z += 0
    
    x_r = -pi/2.
    y_r = 0
    z_r = 0
    
    quaternion = quaternion_from_euler(x_r, y_r, z_r)
    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]
    
    rospy.loginfo("move robot to start position")
    grasper.move_tip_absolute(pose)
    time.sleep(0.1)
    
    
    rospy.loginfo("move robot around object")
    for _ in range(5):
        grasper.move_tip(z=0.1)
        time.sleep(0.1)
        
    rospy.loginfo("move robot around object")
    for _ in range(6):
        grasper.move_tip(x=0.1)
        time.sleep(0.1)
    

def save_color_image(msg):
    
    num_img = 0

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
        cv2.imwrite('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/color_image_' + str(num_img) + '.png', color_img)
       
    num_img += 1
    
    except CvBridgeError, e:
        print(e)
        

def save_depth_image(msg):
    
    image_number = 0
    
    rospy.loginfo("Recieved depth image for dataset")
    
    # cited code beginning
    # Retrieved from: https://answers.ros.org/question/255413/unable-to-store-the-depth-map-in-32fc1-format/ - 24/07/2018
    # Username: Joy16
    try:
        depth_img = bridge.imgmsg_to_cv2(msg,"passthrough")
        depth_array = np.array(depth_img, dtype=np.float32)
        cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)
        
        cv2.imwrite('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/depth_image_' + str(image_number) + '.png', depth_img)
     # cited code end   
     
    image_number += 1
     
    except CvBridgeError, er: 
        print(er)
        
def save_camera_info(msg):
    rospy.loginfo("Recieved camera info for dataset")
    
    camera_info = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/camera_info.txt', 'w')
    msg_as_string = str(msg)
    camera_info.write(msg_as_string)
            
    camera_info.close()
        
        
def save_dataset():
    
    # The position of the object should be known before creating the dataset
    pose = Pose()
    pose.position.x = 0.15
    pose.position.y = 0
    pose.position.z = 0.772
    
    # color image topic
    image_topic_color_img = "/kinect_sim/camera1/rgb/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_color_img, Image, save_color_image, queue_size=1)
    
    # depth image topic
    image_topic_depth_img = "/kinect_sim/camera1/depth/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_depth_img, Image, save_depth_image, queue_size=1)
    
    # camera info topic
    image_topic_camera_info_img = "/kinect_sim/camera1/rgb/camera_info"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_camera_info_img, CameraInfo, save_camera_info, queue_size=1)

    move_robot_around_object(pose)
    
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    save_dataset()