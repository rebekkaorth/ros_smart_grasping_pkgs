#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from smart_grasping_sandbox.smart_grasper import SmartGrasper

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
     grasper.pick()
     grasper.open_hand()
    
    
        
if __name__ == '__main__':
    try:
        grasp_ball()
        
    except rospy.ROSInterruptException:
        pass