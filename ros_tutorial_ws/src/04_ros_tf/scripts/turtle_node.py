#! /usr/bin/env python

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse, Kill, KillRequest, KillResponse
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
    broadcaster.sendTransform(translation, rotation, rospy.Time().now(), turtle_name, "world")


if __name__ == '__main__':
    # initialize node
    node_name = "turtle_node"
    rospy.init_node(node_name)

    # turtle_name = 'itcast'
    # turtle_x = 1
    # turtle_y = 1
    # turtle_theta = 90

    turtle_name = rospy.get_param('~name', default='itcast')
    turtle_x = rospy.get_param('~x', default=1)
    turtle_y = rospy.get_param('~y', default=1)
    turtle_theta = rospy.get_param('~theta', default=90)

    try:
        # turtlesim/Kill
        kill_client = rospy.ServiceProxy('/kill', Kill)
        kill_client.wait_for_service()
        kill_request = KillRequest()
        kill_request.name = 'turtle1'
        kill_client.call(kill_request)
        kill_client.close()
    except Exception as e:
        print(e)

    # turtlesim/Spawn
    spawn_client = rospy.ServiceProxy('/spawn', Spawn)
    spawn_client.wait_for_service()
    spawn_request = SpawnRequest()
    spawn_request.x = turtle_x
    spawn_request.y = turtle_y
    spawn_request.name = turtle_name
    spawn_request.theta = radians(turtle_theta)
    spawn_client.call(spawn_request)
    spawn_client.close()

    # subscribe turtle pose 
    rospy.Subscriber('/{}/pose'.format(turtle_name), Pose, pose_callback)

    # create a broadcaster for transformation 
    broadcaster = TransformBroadcaster()

    rospy.spin()
