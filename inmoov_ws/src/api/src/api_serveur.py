#! /usr/bin/env python

import rospy, sys
import roslib

from std_msgs.msg import UInt8 # for the publisher

import actionlib
import api.msg

class move_server(object):
  def __init__(self,name):
    self.action_name = name
    self.server = actionlib.SimpleActionServer(self.action_name, api.msg.MoveAction, self.execute, False)
    self.server.start()
    self.feedback = api.msg.MoveFeedback()
    self.result = api.msg.MoveResult()

  def execute(self, goal):
    self.topics = goal.topics
    self.data = goal.data
    
    for i in range(len(self.topics)):
      print("Publishing : " + self.topics[i] + " => " + str(self.data[i]))
      pub = rospy.Publisher(self.topics[i] + "/data", UInt8, queue_size=10)
      print(self.data[i])
      pub.publish(self.data[i])
      rospy.sleep(0.1)

    self.result.success = True

    self.server.set_succeeded(self.result)

if __name__ == '__main__':
  rospy.init_node('api')
  server = move_server(rospy.get_name())
  rospy.spin()
