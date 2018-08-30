#!/usr/bin/env python

# Unit test to test the nn_conector node 

package_name = 'object_grasping'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import unittest
import time
import os 
import rospy
from geometry_msgs.msg import Pose

success = False

class NeuralNetworkConectorTest(unittest.TestCase):
        
    # tests if files are at the directory they are needed at, so they can be used as input for the neural network 
    def file_saving_test(self):
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs/color.png'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs/depth.png'))
        
    # publish sample pose 
    def pose_published(self):
         pub = rospy.Publisher('posePublisher', Pose, queue_size=10)
         rospy.init_node('posePublisher', anonymous=True)
         pub.publish(self.get_pose())

    def callback(self, msg):
        success = False
        if type(msg) is geometry_msgs.msg.Pose:
            success = True
        return success
    
    # test if published pose is equal to sample pose 
    def subscription_test(self):
        rospy.init_node("poseSubscriber", anonymous=True)
        result = rospy.Subscriber("posePublisher", Pose, self.callback)
        timeout_sub = time.time() + 30.0
        while not rospy.is_shutdown() and not success and not time.time() < timeout_sub:
            time.sleep(1.0)
            
        self.assertTrue(result)
        
    
    # sample pose 
    def get_pose():
        pose = Pose()
        pose.position.x = 0.15
        pose.position.y = 0
        pose.position. z = 0.772
        return pose 
        
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'nn_conector_test', NeuralNetworkConectorTest())