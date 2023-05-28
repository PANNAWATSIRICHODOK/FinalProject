#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty, EmptyResponse

def go_home_callback(request):
    rospy.loginfo("Going to home.")
    rospy.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def go_to_kitchen_callback(request):
    rospy.loginfo("Going to kitchen.")
    rospy.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def stop_callback(request):
    rospy.loginfo("Stop!")
    return EmptyResponse()

rospy.init_node('navigation_node')
go_home_service = rospy.Service('/go_home', Empty, go_home_callback)
go_to_kitchen_service = rospy.Service('/go_to_kitchen', Empty, go_to_kitchen_callback)
stop_service = rospy.Service('/stop', Empty, stop_callback)

rospy.spin()
