#!/usr/bin/env python

from __future__ import print_function

import rospy
from std_srvs.srv import Trigger, TriggerResponse


def handle_add_two_ints(req):
    print("Returning ")
    
    return TriggerResponse(
        success=True,
        message="Hey, roger that; we'll be right there!"
    )

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', Trigger, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()