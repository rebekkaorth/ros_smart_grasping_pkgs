#!/usr/bin/env python

# Unit test to test the object_grasper node 

package_name = 'object_grasping'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import unittest
import os 
import rospy
from geometry_msgs.msg import Pose
import object_grasping

class ObjectGrasperTest(unittest.TestCase):
        
    # test if published pose by connector equals the test pose 
    def pose_published_test(self):
        self.publish_pose()
        assertEqual(self.sub_pose(), self.get_pose)
    
    # publish pose of nn_connector
    def publish_pose(self):
        pub = rospy.Publisher('posePub', Pose, queue_size=10)
        rospy.init_node('posePub', anonymous=True)
        pub.publish(self.get_pose)
    
    # subscribe to the pose published by the nn_connector 
    def subscribe_pose(self):
       return object_grasper.get_pose().pose  
    
    # test pose 
    def get_pose(self):
        pose = Pose()
        pose.position.x = 0.15
        pose.position.y = 0
        pose.position. z = 0.772
        return pose 
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'object_grasper_test', ObjectGrasperTest)