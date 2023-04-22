#! /usr/bin/env python

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from math import radians
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tf.broadcaster import TransformBroadcaster
from tf.transformations import quaternion_from_euler


def pose_callback(msg):
    if not isinstance(msg, Pose): return

    # turtle and world frame relationship
    #  msg.x msy.y
    #  msg.theta
    # translation: describe pose 
    translation = (msg.x, msg.y, 0)
    # rotation: describe altitude
    # euler -> quaternion
    rotation = quaternion_from_euler(0, 0, msg.theta)
    # time: time stamp
    # child: turtle frame
    # parent: world frame
    broadcaster.sendTransform(translation, rotation, rospy.Time().now(), "frame_a", "world")


if __name__ == '__main__':
    # initialize node
    node_name = "turtle_a_ctrl_node"
    rospy.init_node(node_name)

    # subscribe pose of turtle
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    # create a broadcaster to broadcast tf
    broadcaster = TransformBroadcaster()

    # spin the program
    rospy.spin()
