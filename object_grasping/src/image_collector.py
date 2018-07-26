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
        
def grasp_ball(): 
    print(grasper.get_object_pose())
     
    rospy.loginfo("Moving to Pregrasp")
     
    grasper.open_hand()
    time.sleep(0.1)
        
    ball_pose = grasper.get_object_pose()
    ball_pose.position.x = -0.472 
    ball_pose.position.y = 0.159
    ball_pose.position.z = 0.772
    ball_pose.position.z += 0.5
        
    print(ball_pose.position)
        
    #setting an absolute orientation (from the top)
    quaternion = quaternion_from_euler(-pi/2., 0.0, 0.0)
    ball_pose.orientation.x = quaternion[0]
    ball_pose.orientation.y = quaternion[1]
    ball_pose.orientation.z = quaternion[2]
    ball_pose.orientation.w = quaternion[3]
        
    grasper.move_tip_absolute(ball_pose)
    time.sleep(0.1)
        
    rospy.loginfo("Grasping")
    grasper.move_tip(y=-0.164)
    time.sleep(0.1)
    grasper.check_fingers_collisions(False)
    time.sleep(0.1)
    grasper.close_hand()
    time.sleep(0.1)
        
    rospy.loginfo("Lifting")
    for _ in range(5):
        grasper.move_tip(y=0.01)
        time.sleep(0.1)
            
    grasper.check_fingers_collisions(True)
     
     
    grasper.open_hand()
    
    
        
if __name__ == '__main__':
    try:
        grasp_ball()
        
    except rospy.ROSInterruptException:
        pass