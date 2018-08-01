#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from smart_grasping_sandbox.smart_grasper import SmartGrasper
import time
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler
from math import pi, cos, sin

class ObjectGrasping(object): 
    
    rospy.init_node("object_grasping_lib")
    
    
    grasper = SmartGrasper()

    def lift_object(pose): 
        
        rospy.loginfo("lift object up")
        time.sleep(1)
        
        for _ in range(10):
            grasper.move_tip(y=0.1)
            time.sleep(0.1)
        
    def move_object_to_location(pose, x, y, z):
        
        rospy.loginfo("move object to the right")
        time.sleep(1)
            
        for _ in range(20):
            grasper.move_tip(x=0.1)
            time.sleep(0.1)
            
        rospy.loginfo("move object down")
        time.sleep(1)
            
        for _ in range(10):
            grasper.move_tip(y=-0.1)
            time.sleep(0.1)
            
        grasper.open_hand()
        grasper.check_fingers_collisions(False)
        
            
    def grasp_ball(x, y, z, x_r, y_r, z_r, w=0):
        
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
        time.sleep(1)
        
        rospy.loginfo("opening hand")
        grasper.open_hand()
        time.sleep(1)
        
        rospy.loginfo("move tool tip to object pose")
        grasper.move_tip(y=-0.164)
        time.sleep(1)
        print("tip pose 2: {tippose}").format(tippose=grasper.get_tip_pose())
        time.sleep(1)
        
        rospy.loginfo("check if hand is open")
        grasper.check_fingers_collisions(False)
        time.sleep(1)
        
        rospy.loginfo("close hand")
        grasper.close_hand()
        time.sleep(1)
            