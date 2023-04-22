#!/usr/bin/env python

# import ros environment
import rospy

if __name__ == '__main__':
    # initialize ros node, need to specify node name
    rospy.init_node('itcast_node')

    # rate , 10 hz: 10 times per second
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        print('hello ros python')
        rate.sleep()

    rospy.spin()
