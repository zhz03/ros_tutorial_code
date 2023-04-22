#! /usr/bin/env python

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from math import radians
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tf.broadcaster import TransformBroadcaster
from tf.transformations import quaternion_from_euler
from math import sin, cos, radians


if __name__ == '__main__':
    # initialize node
    node_name = "circle_node"
    rospy.init_node(node_name)

    broadcaster = TransformBroadcaster()

    # radio of circuit 
    r = 3.0
    theta = 0

    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        x = r * cos(radians(theta))
        y = r * sin(radians(theta))

        # translation: position
        translation = (x, y, 0)
        # rotation: 
        # euler -> quaternion
        rotation = quaternion_from_euler(0, 0, 0)
        # time stamp
        # child: turtle frame
        # parent: world frame 
        broadcaster.sendTransform(translation, rotation, rospy.Time().now(), "circle", "turtle_a")

        rate.sleep()

        theta += 1

    rospy.spin()
