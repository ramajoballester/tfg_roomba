#!/usr/bin/env python3
import rospy
import tfg_roomba.msg
import pygame

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print ('Initialised Joystick : %s' % joystick.get_name())

# pygame.display.set_mode((200, 200))

if __name__ == '__main__':
    rospy.init_node('joystick_controller')

    pub = rospy.Publisher('axis', tfg_roomba.msg.Joystick, queue_size=1)
    rate = rospy.Rate(50.0)

    numaxes = joystick.get_numaxes()
    print("numaxes")
    print(numaxes)
    print("--------------")

    numbuttons = joystick.get_numbuttons()
    print("numbuttons")
    print(numbuttons)
    print("--------------")

    while not rospy.is_shutdown():
        cmd = tfg_roomba.msg.Joystick()
        pygame.event.pump()
        cmd.l3x = joystick.get_axis(0)
        cmd.l3y = joystick.get_axis(1)
        cmd.r3x = joystick.get_axis(3)
        cmd.r3y = joystick.get_axis(4)


        pub.publish(cmd)

        rate.sleep()
