#!/usr/bin/env python

# Unit test to test the object_grasper node 

package_name = 'object_grasping'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import time
import rostest
import unittest
import os 
import rospy
from geometry_msgs.msg import Pose

success = False

class ObjectGrasperTest(unittest.TestCase):
        
    def callback(self, msg):
        success = False
        print(type(msg))
        if type(msg) is geometry_msgs.msg.Pose:
            success = True
        return success
    
    # test if subscription works and if the correct Pose is returned
    def subscription_test(self):
        rospy.init_node("poseSubscriber", anonymous=True)
        result = rospy.Subscriber("posePublisher", Pose, self.callback)
        timeout_sub = time.time() + 30.0
        while not rospy.is_shutdown() and not success and not time.time() < timeout_sub:
            time.sleep(1.0)
            
        self.assertTrue(result)
    
    # sample pose 
    def get_pose(self):
        pose = Pose()
        pose.position.x = 0.15
        pose.position.y = 0
        pose.position. z = 0.772
        return pose 
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'object_grasper_test', ObjectGrasperTest)