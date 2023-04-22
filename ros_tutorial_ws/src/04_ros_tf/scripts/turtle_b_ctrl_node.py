#! /usr/bin/env python
# coding: utf-8

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from math import radians
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tf.broadcaster import TransformBroadcaster
from tf.transformations import quaternion_from_euler
from tf.listener import TransformListener
from math import sqrt, atan2
from std_msgs.msg import Float32


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
    broadcaster.sendTransform(translation, rotation, rospy.Time().now(), "frame_b", "world")


if __name__ == '__main__':
    # initialize node
    node_name = "turtle_b_ctrl_node"
    rospy.init_node(node_name)

    # turtlesim/Spawn
    spawn_client = rospy.ServiceProxy('/spawn', Spawn)
    spawn_client.wait_for_service()
    spawn_request = SpawnRequest()
    spawn_request.x = 1
    spawn_request.y = 1
    spawn_request.name = 'mobility'
    spawn_request.theta = radians(90)
    spawn_client.call(spawn_request)
    spawn_client.close()

    # test motion of turtle B geometry_msgs/Twist
    publisher = rospy.Publisher('/mobility/cmd_vel', Twist, queue_size=10)

    # Subscribe to the position and orientation of turtle B
    rospy.Subscriber('/mobility/pose', Pose, pose_callback)

    # Create a coordinate relationship broadcaster
    broadcaster = TransformBroadcaster()

    # Create a coordinate relationship listener
    listener = TransformListener()

    # Test to observe changes in distance
    distance_pub = rospy.Publisher('/test/distance', Float32, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            # function parameters:
            # target_frame: parent frame 
            # source_frame: child frame
            # time: closet timestamp
            # Function return: position[x, y, z], quaternion[x, y, z, w]

            transform = listener.lookupTransform('frame_b', 'frame_a', rospy.Time())
            x, y, z = transform[0]

            # linear distance
            distance = sqrt(x ** 2 + y ** 2)
            angular = atan2(y, x)

            # msg = Float32()
            # msg.data = distance
            # distance_pub.publish(msg)
            distance_pub.publish(Float32(data=distance))

            # vel = distance / time
            twist = Twist()
            twist.linear.x = 1.0 * distance
            twist.angular.z = 2.0 * angular
            publisher.publish(twist)
        except Exception as e:
            print(e)

        rate.sleep()

    rospy.spin()
