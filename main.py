#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty

rospy.init_node('main_node')

rospy.wait_for_service('/go_to_kitchen')
go_to_kitchen = rospy.ServiceProxy('/go_to_kitchen', Empty)
go_to_kitchen()

rospy.wait_for_service('/stop')
stop = rospy.ServiceProxy('/stop', Empty)
stop()

rospy.wait_for_service('/go_home')
go_home = rospy.ServiceProxy('/go_home', Empty)
go_home()

rospy.wait_for_service('/stop')
stop()
