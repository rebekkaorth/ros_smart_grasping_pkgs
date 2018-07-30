#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from smart_grasping_sandbox.smart_grasper import SmartGrasper
import time
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler
from math import pi, cos, sin

grasper = SmartGrasper()

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "Hello World %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        
def grasp_ball(x, y, z, x_r, y_r, z_r, w=0):
    print(type(grasper.get_object_pose()))
    print(grasper.get_object_pose())
    print("position: {x}, {y}, {z}").format(x=x, y=y, z=z) 
    print("tip pose: {tippose}").format(tippose=grasper.get_tip_pose())
    
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
    
    rospy.loginfo("lift object")
    for _ in range(10):
        grasper.move_tip(y=0.01)
        time.sleep(0.1)
        
    grasper.check_fingers_collisions(True)
        
        
if __name__ == '__main__':
    try:
        x = 0.069
        y = 0
        z = 1
        pitch = 0
        yaw = 0
        x_r = cos(yaw) * cos(pitch)
        y_r = sin(yaw) * cos(pitch)
        z_r = sin(pitch)
        w = 0.75
        grasp_ball(x, y, z, x_r, y_r, z_r, w)
        
    except rospy.ROSInterruptException:
        pass