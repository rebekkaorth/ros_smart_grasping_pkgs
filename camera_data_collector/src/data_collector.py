import rospy
from smart_grasping_sandbox.smart_grasper import SmartGrasper 


def get_pose(): 
    grasper = SmartGrasper
    print(grasper.get_pose)


get_pose()
