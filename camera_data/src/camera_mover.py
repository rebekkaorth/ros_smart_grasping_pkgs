#!/usr/bin/env python

# node to move the camera when creating datasets of objects in the simulation
# It uses the "Smart Grasping" library to plan motions.
# It assumes that objects are placed on the right lower corner of the table in 
# the simulation.
# It moves around the object in approximately 90 degrees. 

import rospy 
import numpy as np
from smart_grasping_sandbox.smart_grasper import SmartGrasper
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler
from math import pi, cos, sin

bridge = CvBridge()

def move_robot_around_object(grasper):
    
    rospy.loginfo("move robot around object")
    #movement of the robotic arm 
    for _ in range(5):
        grasper.move_tip(z=0.1) 
        time.sleep(0.1)
        
    rospy.loginfo("move robot around object")
    for _ in range(6):
        grasper.move_tip(x=0.1)
        time.sleep(0.1)
        
def move_to_start_pose(pose, grasper): 
    
    #adjust positional value of pose to place arm next to the object
    pose.position.x += 0.3
    pose.position.y += 0.1
    pose.position.z += 0
    
    x_r = -pi/2.
    y_r = 0
    z_r = 0
    
    # calculate orientation values
    quaternion = quaternion_from_euler(x_r, y_r, z_r) 
    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]
    
    rospy.loginfo("move robot to start position")
    grasper.move_tip_absolute(pose) # move arm to intended pose
    time.sleep(0.1)
    
        
def camera_mover():
    
    # Position of the object in the scene
    pose = Pose()
    pose.position.x = 0.15
    pose.position.y = 0
    pose.position.z = 0.772
    
    grasper = SmartGrasper()
    
    move_to_start_pose(pose, grasper) # starting position is right next to the object
    move_robot_around_object(grasper) # moves robotic arm aroun object in a 90 degree angle
    
    # prevents node from stopping before ctrl + c is pressed
    rospy.spin()

if __name__ == '__main__':
    camera_mover()