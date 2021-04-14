#! /usr/bin/env python
import rospy
import roslib
roslib.load_manifest('api')

from std_msgs.msg import UInt8
import json

import actionlib

import api.msg

from configs.configs import Config
from utils.json_utils import Value_Finder, Reader

class api_client:
    def __init__(self):
        self.config = Config()
        self.control_json = self.config.get_control_json()
        self.topics = self.config.get_topics()
        self.data = []
        self.load_data()

        self.client = actionlib.SimpleActionClient("api", api.msg.MoveAction)

        self.goal = api.msg.MoveGoal()

        self.client.wait_for_server()

    def get_control_json(self):
        return self.control_json


    def update_control_json(self, new_control_json):
        print(new_control_json)
        self.control_json = new_control_json
        self.load_data()

    def send_goal(self):
        self.goal.topics = self.topics
        self.goal.data = self.data

        self.client.send_goal(self.goal)

        self.client.wait_for_result()
        return self.client.get_result()

    def send_goal_from_file(self):
        self.control_json = Reader(self.config.pkg + "/api/control/inmoov_control.json").js
        self.load_data()
        result = self.send_goal()
        return result

    def load_data(self):
        for i in range(0, len(self.topics)):
            data = Value_Finder(self.control_json, self.topics[i]).value
            msg = UInt8(data)
            self.data.insert(i, msg)

if __name__ == '__main__':
    rospy.init_node('api_node_client')  

    result = api_client()

    result.send_goal_from_file()
    rospy.spin()
    """try:
        rospy.init_node('api_node_client')  

        result = api_client()

        result = result.send_goal_from_file()
        print(result)

    except rospy.ROSInterruptException:
        print("program interrupted before completion")"""
    

    """def move_client(self, order):
        client = actionlib.SimpleActionClient("api", api.msg.MoveAction)
        client.wait_for_server()
        goal = api.msg.MoveGoal(order=order)
        client.send_goal(goal)
        client.wait_for_result()
        return client.get_result()"""
