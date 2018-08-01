#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from smart_grasping_sandbox.smart_grasper import SmartGrasper
import time
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler
from math import pi, cos, sin

grasper = SmartGrasper()


def node_init():
    rospy.init_node('object_grasper', anonymous=True)
    
    sub = rospy.Subscriber('smart_grasper', String, queue_size=10)
    

def lift_object(pose): 
    
    rospy.loginfo("lift object up")
    time.sleep(1)
    
    for _ in range(10):
        grasper.move_tip(y=0.1)
        time.sleep(0.1)
    
def move_object_to_location(pose, x, y, z):
    
    rospy.loginfo("move object to the right")
    time.sleep(1)
        
    for _ in range(15):
        grasper.move_tip(x=0.1)
        time.sleep(0.1)
    
    grasper.move_tip(x=0.15, y=0, z=0.784)
        
    rospy.loginfo("move object down")
    time.sleep(1)
        
    for _ in range(10):
        grasper.move_tip(y=-0.1)
        time.sleep(0.1)
        
    grasper.open_hand()
    grasper.check_fingers_collisions(False)
    
        
def grasp_object(x=0, y=0, z=0, x_r=0, y_r=0, z_r=0, w=0):
    
    object_pose = Pose()
    
    object_pose.position.x = x
    object_pose.position.y = y
    object_pose.position.z = z
    
    object_pose.position.z += 0.5
    
    object_pose.orientation.x = x_r
    object_pose.orientation.y = y_r
    object_pose.orientation.z = z_r
    object_pose.orientation.w = 0 
    
    quaternion = quaternion_from_euler(-pi/2., 0.0, 0.0)
    object_pose.orientation.x = quaternion[0]
    object_pose.orientation.y = quaternion[1]
    object_pose.orientation.z = quaternion[2]
    object_pose.orientation.w = quaternion[3]
    
    grasper.move_tip_absolute(object_pose)
    time.sleep(0.1)
    
    rospy.loginfo("opening hand")
    grasper.open_hand()
    time.sleep(0.1)
    
    rospy.loginfo("move tool tip to object pose")
    grasper.move_tip(y=-0.164)
    time.sleep(0.1)
    
    rospy.loginfo("check if hand is open")
    grasper.check_fingers_collisions(False)
    time.sleep(0.1)
    
    rospy.loginfo("close hand")
    grasper.close_hand()
    time.sleep(0.1)
    grasper.check_fingers_collisions(True)
    
    lift_object(object_pose)
    
        
if __name__ == '__main__':
    
    try:
        x = -0.23
        y = 0.159
        z = 0.772
        pitch = -0.001
        yaw = 0
        
        # calculating Euler angles from the rotation values as radiants 
        x_r = cos(yaw) * cos(pitch)
        y_r = sin(yaw) * cos(pitch)
        z_r = sin(pitch)
        
        w = 0
        
        grasp_object(x, y, z, x_r, y_r, z_r, w)
        
    except rospy.ROSInterruptException:
        pass