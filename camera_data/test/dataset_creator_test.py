#!/usr/bin/env python

# Unit test to test the color_image_saver node 

package_name = 'camera_data'

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import unittest
import os 

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
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'dataset_maker_test', DatasetMakerSaverTest)