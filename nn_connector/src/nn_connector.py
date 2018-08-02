#!/usr/bin/env python

# this services uses output of:
#   color_image_svaer.py
#   depth_image_saver.py
#   camera_info_saver.py 
# in order to use this service properly these nodes need to be run first

import rospy
from geometry_msgs.msg import Point

# the following function and its content is merely an example and a place holder for the function
# that uses a working neural network

def predict_object_pose():
    # get the images taken by the camera 
    color_img = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs/color.png', 'w')
    print("service of neural network has recevied a color image")
    depth_img = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs/depth.png', 'w')
    print("service of neural network has recevied a depth image")
    camera_info = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt', 'w')
    print("service of neural network has recevied camera information")
    
    # call neural network and provide images as input 
    
    # As long as the neural network is not yet implemented the following output will be returned
    # The following variables represent the (predicted) pose of the object 
    point = Point() 
    point.x = 0.15 
    point.y = 0
    point.z = 0.772

    return point
    

def predict_object_pose_server():
    
    pub_nn_output = rospy.Publisher('pub_nn_output', Point, queue_size=10)
    
    rospy.init_node('predict_object_pose_server', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub_nn_output.publish(predict_object_pose())
        rate.sleep()


if __name__ == "__main__":
    predict_object_pose_server()