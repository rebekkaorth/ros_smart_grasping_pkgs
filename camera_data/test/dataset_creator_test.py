#!/usr/bin/env python

# Unit test to test the dataset_creator node.
# It tests the presence of the saving path as well as if a fie was saved in 
# that directory.
# It also tests the subscription to the Kinect camera topic in terms of if the
# correct object is recevied. 

package_name = 'camera_data'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import rostest
import rospy
import time
from sensor_msgs.msg import CameraInfo
from sensor_msgs.msg import Image
import unittest
import os 

success_color = False
success_depth = False
success_info = False

class DatasetMakerSaverTest(unittest.TestCase):
    
    # tests if the path the file is supposed to be saved at exists 
    def path_correctness_test(self):
        self.assertTrue(os.path.isdir('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset-images'))
        
    # tests if the file as saved correctly
    def file_saving_test(self):
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset-images/color-image-1.png'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset-images/depth-image-1.png'))
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset-images/camera-info-1.txt'))
        
        self.assertFalse(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset-images/color-image-01.png'))
        self.assertFalse(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset-images/depth-image-01.png'))
        self.assertFalse(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/dataset-images/camera-info-01.txt'))
        
    def callback_color(self, msg):
        success_color = False
        global sensor_msgs
        if type(msg) is sensor_msgs.msg._Image.Image: # test if correct object is received
            success = True
        return success_color
    
    def callback_depth(self, msg):
        global sensor_msgs
        success_depth = False
        if type(msg) is sensor_msgs.msg._Image.Image:  # test if correct object is received
            success = True
        return success_depth
        
    def callback_info(self, msg):
        global sensor_msgs
        success_info = False
        if type(msg) is sensor_msgs.msg._CameraInfo.CameraInfo:  # test if correct object is received
            success = True
        return success_info
    
    def subscription_test(self):
        # node name
        rospy.init_node("color_img_sub_test", anonymous=True)
        
        # test if subscription return Image object (for color images)
        result_color = rospy.Subscriber("/kinect_sim/camera1/rgb/image_raw", Image, self.callback_color)
        timeout_sub = time.time() + 20.0
        while not rospy.is_shutdown() and not success_color and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result_color)
        
        # test if subscription return Image object (for depth images)
        result_depth = rospy.Subscriber("/kinect_sim/camera1/depth/image_raw", Image, self.callback_depth)
        while not rospy.is_shutdown() and not success_depth and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result_depth)
        
        # test if subscription return CameraInfo object 
        result_info = rospy.Subscriber("/kinect_sim/camera1/rgb/camera_info", CameraInfo, self.callback_info)
        while not rospy.is_shutdown() and not success_info and not time.time() < timeout_sub:
            time.sleep(1.0)
        self.assertTrue(result_info)
        
    

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'dataset_maker_test', DatasetMakerSaverTest)