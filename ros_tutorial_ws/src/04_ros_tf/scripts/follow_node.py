#! /usr/bin/env python

import rospy
from tf.listener import TransformListener
from geometry_msgs.msg import Twist
from math import sqrt, atan2


if __name__ == '__main__':
    # initialize node
    node_name = "follow_node"
    rospy.init_node(node_name)

    # follower
    follow = rospy.get_param('~follow', default='ucla')
    # leader
    parent = rospy.get_param('~parent', default='mobility')

    # Create a listener of transformation
    listener = TransformListener()

    # test motion of turtle B geometry_msgs/Twist
    publisher = rospy.Publisher('/{}/cmd_vel'.format(follow), Twist, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            # parameters:
            # target_frame: parent frame
            # source_frame: children frame
            # time: closest time 
            # return parameters: position [x, y, z], quaternion[x, y, z, w]

            transform = listener.lookupTransform(follow, parent, rospy.Time())
            x, y, z = transform[0]

            # linear distance
            distance = sqrt(x ** 2 + y ** 2)
            angular = atan2(y, x)

            # vel = distance / time
            twist = Twist()
            twist.linear.x = 1.0 * distance
            twist.angular.z = 2.0 * angular
            publisher.publish(twist)
        except Exception as e:
            print(e)

        rate.sleep()

    rospy.spin()
