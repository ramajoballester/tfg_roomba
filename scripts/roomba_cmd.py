#!/usr/bin/env python3
import rospy
import tfg_roomba.msg
from geometry_msgs.msg import Twist

vel_max = 0.5
w_max = 1.0
vel = 0
w = 0

def callback(msg):
    global vel, w
    vel = msg.r3y * (-1) * vel_max
    w = msg.l3x * (-1) * w_max


if __name__ == '__main__':
    rospy.init_node('roomba_cmd')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10.0)

    cmd = Twist()
    cmd.linear.x = 0
    cmd.linear.y = 0
    cmd.linear.z = 0
    cmd.angular.x = 0
    cmd.angular.y = 0
    cmd.angular.z = 0

    rospy.Subscriber('axis', tfg_roomba.msg.Joystick, callback)

    while not rospy.is_shutdown():
        cmd.linear.x = vel
        cmd.angular.z = w
        pub.publish(cmd)
        rate.sleep()
