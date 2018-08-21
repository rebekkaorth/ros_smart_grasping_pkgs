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
        
def camera_mover():
    
    # The position of the object should be known before creating the dataset
    pose = Pose()
    pose.position.x = 0.15
    pose.position.y = 0
    pose.position.z = 0.772

    move_robot_around_object(pose)
    
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    camera_mover()