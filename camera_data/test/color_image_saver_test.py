#!/usr/bin/env python

# Unit test to test the color_image_saver node 

package_name = 'camera_data'

import sys
import unittest
import os 

class ColorImageSaverTest(unittest.TestCase):
    
    # tests if the path the file is supposed to be saved at exists 
    def path_correctness_test(self):
        self.assertTrue(os.path.isdir('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs'))
        
    # tests if the file as saved correctly
    def file_saving_test(self):
        self.assertTrue(os.path.isfile('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs/color.png'))
        

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(package_name, 'color_image_saver_test', ColorImageSaverTest)
