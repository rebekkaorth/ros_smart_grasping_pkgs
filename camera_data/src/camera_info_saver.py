#!/usr/bin/env python

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import CameraInfo
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import numpy as np
        
def save_camera_info_callback(msg):
    
    rospy.loginfo("camera info received!")
    
    camera_info = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt', 'w')
    print(type(msg))
    msg_as_string = str(msg)
    camera_info.write(msg_as_string)
            
    camera_info.close()
        

def info_saver():
    rospy.init_node('camera_info_listener')
    
    # Define your image topic
    image_topic_camera_info = "/kinect_sim/camera1/rgb/camera_info"
    
    
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_camera_info, CameraInfo, save_camera_info_callback, queue_size=1)
    
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    info_saver()