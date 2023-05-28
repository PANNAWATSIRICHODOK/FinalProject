#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty, EmptyResponse

def charging(request):
    rospy.loginfo("Going to charging station.")
    rospy.sleep(2)
    rospy.loginfo("finished.")
    return EmptyResponse()

rospy.init_node('additional_node')
additional_service = rospy.Service('/charg', Empty, charging)

rospy.spin()
