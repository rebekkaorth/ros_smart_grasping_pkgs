#!/usr/bin/env python

# node to grasp objects and place them at a given point based on a Pose-object
# received by the nn_connector node. 

import rospy
from smart_grasping_sandbox.smart_grasper import SmartGrasper
import time
from geometry_msgs.msg import Pose, Point
from tf.transformations import quaternion_from_euler
from math import pi, cos, sin

grasper = SmartGrasper()

def lift_object(pose): 
    
    rospy.loginfo("lift object up")
    
    # lift robotic arm up
    for _ in range(12):
        grasper.move_tip(y=0.1)
        time.sleep(0.1)
    
def move_object_to_location(pose):
    
    rospy.loginfo("move object to the right")
    time.sleep(1)
    
    # move robotic arm to the the left    
    for _ in range(10):
        grasper.move_tip(x=0.1)
        time.sleep(0.1)
        
    rospy.loginfo("move object down")
    time.sleep(1)
    
    # move robotic arm down    
    for _ in range(10):
        grasper.move_tip(y=-0.1)
        time.sleep(0.1)
    
    # release object by opening robotic hand    
    grasper.open_hand()
    grasper.check_fingers_collisions(False)
    
        
def grasp_object(object_pose):
    
    # set z pose higher to prevent collisions
    object_pose.position.z += 0.5
    
    x_r = -pi/2.
    y_r = 0
    z_r = 0
    
    # calculate quaternions for orientation values
    quaternion = quaternion_from_euler(x_r, y_r, z_r)
    object_pose.orientation.x = quaternion[0]
    object_pose.orientation.y = quaternion[1]
    object_pose.orientation.z = quaternion[2]
    object_pose.orientation.w = quaternion[3]
    
    # move robotic arm to object pose
    rospy.loginfo("move arm to object pose")
    grasper.move_tip_absolute(object_pose)
    
    # open hand to enable grasp
    rospy.loginfo("opening hand")
    grasper.open_hand()
    
    # move down to close fingers around object
    rospy.loginfo("move tool tip to object pose")
    grasper.move_tip(y=-0.164)
    time.sleep(0.1)
    
    rospy.loginfo("check if hand is open")
    grasper.check_fingers_collisions(False)
    
    rospy.loginfo("close hand")
    grasper.close_hand()
    time.sleep(0.1)
    grasper.check_fingers_collisions(True)
    
    lift_object(object_pose)
    
    move_object_to_location(pose)  # the middle of the table 
     
def get_pose():
 
    # waits for message from nn_connector 
    pose = rospy.wait_for_message("posePublisher", Pose)
    rospy.loginfo('pose received')
    grasp_object(pose)
    
    # stops node from exiting
    rospy.spin()


if __name__ == '__main__':
    
    try:
        # pose for testing grasping
        pose = Pose()
        pose.position.x = 0.15
        pose.position.y = 0
        pose.position.z = 0.772
        grasp_object(pose)
        
        # get_pose()
        
    except rospy.ROSInterruptException:
        pass