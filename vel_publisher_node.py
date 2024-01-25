#!/usr/bin/env python3

# import the ROS library into this node
import rospy
# import the geometry msg Twist from ROS libraries
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	
	#define a publisher fro sending velocity commands
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	# initialize the node
	rospy.init_node('vel_publisher_node', anonymous=True)
	
	# create a loop rate (timer)
	# set the freuquency at 10 Hz
	roop_rate = rospy.Rate(10)
	# create a message for sending the commands
	vel_cmd = Twist()
	
	# print('Hi')
	# set up a control loop
	while not rospy.is_shutdown():
		# set the linear velocity 
		vel_cmd.linear.x = 1.0
		# set the angular velocity
		vel_cmd.angular.z = 0.5
		
		# publish the message
		cmd_pub.publish(vel_cmd)
		# sleep fro sometime until the next iteration
		roop_rate.sleep()
