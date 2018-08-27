#!/usr/bin/env python

# Unit test to test the color_image_saver node 

package_name = 'camera_data'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import rostest
import rospy
import time
from sensor_msgs.msg import CameraInfo, Image
import unittest
import os 

success_color = False
success_depth = False
success_info = False

class DatasetMakerSaverTest(unittest.TestCase):
    
    # tests if the path the file is supposed to be saved at exists 
    def path_correctness_test(self):
        self.assertTrue(os.path.isdir('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images'))
        
    # tests if the file as saved correctly
    def file_saving_test(self):
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/color_image_0.png'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/depth_image_0.png'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/camera_info_0.txt'))
        
        self.assertFalse(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/color_image_-1.png'))
        self.assertFalse(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/depth_image_-1.png'))
        self.assertFalse(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset_images/camera_info_-1.txt'))
        
    def callback_color(self, msg):
        success_color = False
        if type(msg) is sensor_msgs.msg._Image.Image:
            success = True
        return success_color
    
    def callback_depth(self, msg):
        success_depth = False
        if type(msg) is sensor_msgs.msg._Image.Image:
            success = True
        return success_depth
        
    def callback_info(self, msg):
        success_info = False
        if type(msg) is sensor_msgs.msg._Image.Image:
            success = True
        return success_info
    
    def subscription_test(self):
        rospy.init_node("color_img_sub_test", anonymous=True)
        result_color = rospy.Subscriber("/kinect_sim/camera1/rgb/image_raw", Image, self.callback_color)
        timeout_sub = time.time() + 20.0
        while not rospy.is_shutdown() and not success_color and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result_color)
        
        result_depth = rospy.Subscriber("/kinect_sim/camera1/depth/image_raw", Image, self.callback_depth)
        while not rospy.is_shutdown() and not success_depth and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result_depth)
        
        result_info = rospy.Subscriber("/kinect_sim/camera1/rgb/camera_info", CameraInfo, self.callback_info)
        while not rospy.is_shutdown() and not success_info and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result_info)
        
    

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'dataset_maker_test', DatasetMakerSaverTest)