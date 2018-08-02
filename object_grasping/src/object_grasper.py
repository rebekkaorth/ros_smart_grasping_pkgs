#!/usr/bin/env python

import rospy
from smart_grasping_sandbox.smart_grasper import SmartGrasper
import time
from geometry_msgs.msg import Pose, Point
from tf.transformations import quaternion_from_euler
from math import pi, cos, sin

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
    
        
def grasp_object(object_pose):
    
    # rospy.init_node('object_grasper', anonymous=True)
    
    # sub = rospy.Subscriber('smart_grasper', String, queue_size=10)
    
    # object_pose = Pose()
    
    # object_pose.position.x = x
    # object_pose.position.y = y
    # object_pose.position.z = z
    
    object_pose.position.z += 0.9
    
    x_r = -pi/2.
    y_r = 0
    z_r = 0
    
    quaternion = quaternion_from_euler(x_r, y_r, z_r)
    object_pose.orientation.x = quaternion[0]
    object_pose.orientation.y = quaternion[1]
    object_pose.orientation.z = quaternion[2]
    object_pose.orientation.w = quaternion[3]
    
    rospy.loginfo("move arm to object pose")
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
    
    # lift_object(object_pose)
    
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    rospy.loginfo(data.position.x)
    grasp_object(data)
     
def listener():
 
    # rospy.init_node('listener', anonymous=True)
 
    rospy.Subscriber("chatter", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    
    try:
        pose = Pose()
        pose.position.x = -0.472
        pose.position.y = 0.159
        pose.position.z = 0.772
        grasp_object(pose)
        
        # listener()
        
    except rospy.ROSInterruptException:
        pass