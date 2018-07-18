#!/usr/bin/env python

'''
http://wiki.ros.org/rospy_tutorials/Tutorials/WritingImagePublisherSubscriber - 18/07/2018
''' 

# Python libs
import sys, time

# numpy and scipy
import numpy as np
from scipy.ndimage import filters 

# OpenCV
import cv2 

# ROS libariers 
import roslib
import rospy

VERBOSE = False 

class image_feature: 
    
    def __init__(self):
        
        # Publisher 
        self.image_pub = rospy.Publisher('/output/image_raw', RawImage)
        
        # Subscriber 
        self.subscriber = rospy.Subscriber('/camera/image', RawImage, self.callback, queue_size=1)
        
        if VERBOSE : 
            print ('subscribed to /camera/image')
            
            
    def callback(self, ros_data):
        
        if VERBOSE : 
            print ('received image of type: "%s"' % ros_data.format)
            
        np_arr = np.formstring(ros_data.data, np.unit8)
        
        image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
        
        method = "GridFAST"
        
        feat_det = cv2.FeatureDetector_create(method)
        
        time1 = time.time()
        
        # convert np image to grayscale 
        featPoints = feat_det.detect(
            cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY))
            
        time2 = time.time()
        
        if VERBOSE : 
            print ('%s detector found: %s points in: %s sec.' % (method,
            len(featPoints), time2-time1))
            
        for featpoint in featPoints:
            x, y = featpoint.pt
            cv2.circle(image_np, (int(x), int(y)), 3, (0, 0, 255), -1)
            
        cv2.imshow('cv_img', image_np)
        cv2.waitKey(2)
        
        # Create compressed image
        msg = CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv2.imencode('.jpg', image_np)[1].toString())
        
        # Publish new image 
        self.image_pub.publish(msg)
        
        
def main(args):
    
    ic = image_feature()
    rospy.init_node('image_feature', anonymous=True)
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ('Shutting down ROW image feature detector module')
        
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main(sys.argv)
            