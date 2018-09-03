#!/usr/bin/env python

# node to save depth images. The node subscribes to a topic published by the 
# Kinect camera that porvides depth images. It converts the received data into
# depth image png files. The code citied from other sources is clearly stated 
# below.

# rospy for the subscriber
import rospy
import numpy as np
# ROS Image message
from sensor_msgs.msg import Image, PointCloud2
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2


# Instantiate CvBridge
bridge = CvBridge()

def save_depth_image_callback(msg):
    
    rospy.loginfo("Received an depth image!")

    # cited code beginning
    # Retrieved from: https://answers.ros.org/question/255413/unable-to-store-the-depth-map-in-32fc1-format/ - 24/07/2018
    # Username: Joy16
    try:
        # convert recevied data to png file
        NewImg = bridge.imgmsg_to_cv2(msg,"passthrough")
        depth_array = np.array(NewImg, dtype=np.float32)
        cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)
        cv2.imwrite("/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs/depth.png", depth_array*255)
    # cited code end     
        
    except CvBridgeError, e:
        print(e)


def save_image():
    # name of the nocde
    rospy.init_node('depth_image_listener')
    
    # Define your image topic
    image_topic_color_img = "/kinect_sim/camera1/depth/image_raw"
    
    
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_color_img, Image, save_depth_image_callback, queue_size=1)

    # prevents node from stopping before ctrl + c is pressed
    rospy.spin()

if __name__ == '__main__':
    save_image()