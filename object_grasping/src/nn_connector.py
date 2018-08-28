#!/usr/bin/env python

# this services uses output of:
#   color_image_svaer.py
#   depth_image_saver.py
#   camera_info_saver.py 
# in order to use this service properly these nodes need to be run first

import os.path, sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
import rospy
from geometry_msgs.msg import Pose

# the following function and its content is merely an example and a place holder for the function
# that uses a working neural network
class NN_connector(): 
    
    def predict_object_pose(self):
        
        # open the images taken by the camera 
        color_img = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs/color.png', 'w')
        rospy.loginfo("service of neural network has recevied a color image")
        
        depth_img = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs/depth.png', 'w')
        rospy.loginfo("service of neural network has recevied a depth image")
        
        camera_info = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt', 'w')
        rospy.loginfo("service of neural network has recevied camera information")
        
        # CALL NEURAL NETWORK HERE AND PROVIDE IMAGES AS INPUT 
        
        # As long as the neural network is not yet implemented the following output will be returned
        # The following variables represent the (predicted) pose of the object 
        pose = Pose() 
        pose.position.x = 0.15 
        pose.position.y = 0
        pose.position.z = 0.772
    
        return pose
        
    
    def posePub(self):
        
        pub = rospy.Publisher('posePublisher', Pose, queue_size=10)
        rospy.init_node('posePublisher', anonymous=True)
        predicted_pose = self.predict_object_pose()
        rate = rospy.Rate(1)
        num = 0
        
        while not rospy.is_shutdown() and num < 10:  # gets published 10 times, so object grasper can be called and receive data
            rospy.loginfo(predicted_pose)
            pub.publish(predicted_pose)
            rate.sleep()
            num += 1
        
 
if __name__ == '__main__':
    
    try:
        nnc = NN_conector()
        nnc.posePub()
    
    except rospy.ROSInterruptException:
        pass