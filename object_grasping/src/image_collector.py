#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from smart_grasping_sandbox.smart_grasper import SmartGrasper
import time
from tf.transformations import quaternion_from_euler
from math import pi

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
        
def grasp_ball(x, y, z, roll, pitch, yaw):
    print(type(grasper.get_object_pose()))
    print(grasper.get_object_pose())
    print("position: {x}, {y}, {z}").format(x=x, y=y, z=z) 
    print("orientation: {roll}, {pitch}, {yaw}").format(roll=roll, pitch=pitch, yaw=yaw)
    print("tip pose: {tippose}").format(tippose=grasper.get_tip_pose())
    
    rospy.loginfo("opening hand")
    grasper.open_hand()
    time.sleep(1)
    
    rospy.loginfo("move tool tip to object pose")
    grasper.move_tip(x, y, z, roll, pitch, yaw)
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
        
        
if __name__ == '__main__':
    try:
        grasp_ball(-0.472, 0.159, 0.772, 0.001, -0.001, 0)
        
    except rospy.ROSInterruptException:
        pass