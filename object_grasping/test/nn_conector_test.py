#!/usr/bin/env python

# Unit test to test the nn_conector node 

package_name = 'object_grasping'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import unittest
import os 
import rospy
from geometry_msgs.msg import Pose
import object_grasping

class NeuralNetworkConectorTest(unittest.TestCase):
        
    # tests if files are at the directory they are needed at, so they can be used as input for the neural network 
    def file_saving_test(self):
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs/color.png'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs/depth.png'))
        
    # test if published pose by connector equals the test pose 
    def pose_published_test(self):
        self.publish_pose()
        assertEqual(self.sub_pose(), self.get_pose_for_test)
    
    # publish pose of nn_conector
    def publish_pose(self):
        nn_conector.posePub()
    
    # subscribe to the pose published by the nn_conector 
    def subscribe_pose():
        sub_pose = rospy.wait_for_message("posePublisher", Pose)
        return sub_pose 
    
    # test pose 
    def get_pose():
        pose = Pose()
        pose.position.x = 0.15
        pose.position.y = 0
        pose.position. z = 0.772
        return pose 
        
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'nn_conector_test', NeuralNetworkConectorTest())