#!/usr/bin/env python
'''
this services uses output of:
   color_image_svaer.py
   depth_image_saver.py
   camera_info_saver.py 
in order to use this service properly these nodes need to be run first
'''
import rospy

'''
the following function and its content is merely an example and a place holder for the function
that uses a working neural network
'''
def predict_object_pose(req):
    # get the images taken by the camera 
    color_img = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/color-imgs/color.png', 'w')
    print("service of neural network has recevied a color image" + color_img)
    depth_img = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/depth-imgs/depth.png', 'w')
    print("service of neural network has recevied a depth image" + depth_img)
    camera_info = open('/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/camera-info/camera-info.txt', 'w')
    print("service of neural network has recevied camera information" + camera_info)
    
    # call neural network and provide images as input 
    
    # As long as the neural network is not yet implemented the following output will be returned
    # The following variables represent the (predicted) pose of the object 
    x = 0.15 
    y = 0
    z = 0.772
    return x, y, z 
    
    

def predict_object_pose_server():
    rospy.init_node('predict_object_pose_server')
    
    service = rospy.Service('predict_object_pose', PredictObjectPose, predict_object_pose)
    
    print("ready to predict object pose")
    
    rospy.spin()
    

if __name__ == "__main__":
    predict_object_pose_server()