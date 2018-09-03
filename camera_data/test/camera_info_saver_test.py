#!/usr/bin/env python

# Unit test to test the cmaera_info_saver node. 
# It tests the presence of the saving path as well as if a fie was saved in 
# that directory.
# It also tests the subscription to the Kinect camera topic in terms of if the
# correct object is recevied. 

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import rospy, rostest
from sensor_msgs.msg import CameraInfo
import time
import unittest
import os 

success = False

class CameraInfoSaverTest(unittest.TestCase):
    
    # tests if the path the file is supposed to be saved at exists 
    def path_correctness_test(self):
        self.assertTrue(os.path.isdir('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info'))
        
    # tests if the file ss saved correctly
    def file_saving_test(self):
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt'))
        
    def callback(self, msg):
        success = False
        if type(msg) is sensor_msgs.msg._CameraInfo.CameraInfo:
            success = True
        return success
    
    # test if the subscription returns the correct object
    def subscription_test(self):
        rospy.init_node("cam_info_sub_test", anonymous=True)
        result = rospy.Subscriber("/kinect_sim/camera1/rgb/camera_info", CameraInfo, self.callback)
        timeout_sub = time.time() + 20.0
        while not rospy.is_shutdown() and not success and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result)
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun("camera_data", 'camera_info_saver_test', CameraInfoSaverTest)