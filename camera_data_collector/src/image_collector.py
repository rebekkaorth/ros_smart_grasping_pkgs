 #!/usr/bin/env python

import rospy
from std_msgs.msg import String

def take_image_of_object(): 
    pub = rospy.Publisher('chatter', String, queue_size=10)
       rospy.init_node('talker', anonymous=True)
       rate = rospy.Rate(10) # 10hz
       while not rospy.is_shutdown():
           hello_str = "hello world %s" % rospy.get_time()
           rospy.loginfo(hello_str)
           pub.publish(hello_str)
           rate.sleep()
   
if __name__ == '__main__':
    try:
        take_image_of_object()
    except rospy.ROSInterruptException:
        pass
