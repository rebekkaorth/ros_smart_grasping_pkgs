#!/usr/bin/env python

# Unit test to test the color_image_saver node 

package_name = 'camera_data'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import rostest
import rospy
import time
from sensor_msgs.msg import Image
import unittest
import os 

success = False

class DepthImageSaverTest(unittest.TestCase):
    
    # tests if the path the file is supposed to be saved at exists 
    def path_correctness_test(self):
        self.assertTrue(os.path.isdir('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs'))
        
    # tests if the file as saved correctly
    def file_saving_test(self):
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs/depth.png'))
        
    def callback(self, msg):
        success = False
        if type(msg) is sensor_msgs.msg._Image.Image:
            success = True
        return success
        
    def subscription_test(self):
        rospy.init_node("color_img_sub_test", anonymous=True)
        result = rospy.Subscriber("/kinect_sim/camera1/rgb/image_raw", Image, self.callback)
        timeout_sub = time.time() + 30.0
        while not rospy.is_shutdown() and not success and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result)
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'depth_image_saver_test', DepthImageSaverTest)