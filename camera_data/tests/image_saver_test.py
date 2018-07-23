#!/usr/bin/env python

PKG = 'camera_data'

import sys
import unittest

class ImageSaverTest(unittest.TestCase):
    
    def test_save_image(self):
        
        

if __name__ == '__main__':
    import rosunit
    
    rosunit.unitrun(PKG, 'image_saver_test', ImageSaverTest)
