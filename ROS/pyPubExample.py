#!/usr/bin/env python
#A simple example of sending a ROS topic using python

import rospy 
from std_msgs.msg import String


def talker(commandDir):
    pub = rospy.Publisher('command', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    pub.publish(commandDir)
       

talker("Forward")
