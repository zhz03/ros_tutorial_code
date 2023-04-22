#! /usr/bin/env python

import rospy
import sys


if __name__ == '__main__':
    # initialize node
    node_name = "param_node"
    rospy.init_node(node_name)

    print(sys.argv)

    # #　read param data
    # param = rospy.get_param('version', default='1.110')
    # print param

    # read from node config
    bxg = rospy.get_param('~bxg', default=0)
    print(bxg)

    param = rospy.get_param('~param', default='ok')
    print(param)

    # read from global config /
    bxg = rospy.get_param('/bxg', default=0)
    print(bxg)

    param = rospy.get_param('/param', default='ok')
    print(param)

    rospy.spin()
