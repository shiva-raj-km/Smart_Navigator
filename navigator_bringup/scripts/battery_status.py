#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
import rospy
import actionlib
from move_base_msgs.msg import *

def Charge():
	try:
		simple_move("1.5","0.012","0.06","0.997")
	except rospy.ROSInterruptException:
		print "Keyboard Interrupt"

	print "Charging Point Reached"

def simple_move(x,y,z,w):

    # rospy.init_node('simple_move')

    #Simple Action Client
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()

    #use self?
    #set goal
 
    rospy.loginfo("Set X = "+x)
    rospy.loginfo("Set W = "+w)

    goal.target_pose.pose.position.x = float(x)
    goal.target_pose.pose.position.y = float(y)
    goal.target_pose.pose.orientation.z = float(z)
    goal.target_pose.pose.orientation.w = float(w)
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    #start listner
    rospy.loginfo("Waiting for server")

    sac.wait_for_server()


    rospy.loginfo("Sending Goals")

    #send goal

    sac.send_goal(goal)
    rospy.loginfo("Waiting for server")

    #finish
    sac.wait_for_result()

    #print result
    print(sac.get_result())


def callback(data):
	# rospy.loginfo(data.data)
	if(data.data == True):
		Charge()

def listen():

	rospy.init_node('battery_status',anonymous=True)
	rospy.Subscriber("charge",Bool,callback,queue_size=10)
	rospy.spin()

if __name__ == '__main__':
	listen()