#!/usr/bin/python3
#-*- coding: utf-8 -*-

import rospy, json, websockets, asyncio, sys
from std_msgs.msg import String

from api_client import api_client

def get_all_paths(tree, cur=()):
	if not tree or 'items' not in dir(tree):
		yield cur
	else:
		for n, s in tree.items():
			for path in get_all_paths(s, cur+(n,)):
				yield path

class WSServer:
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.client = api_client()

	def start(self):
		return websockets.serve(self.handler, self.host, self.port)

	async def handler(self,websocket, path):
		name = await websocket.recv()
		print(f"< {name}")

		greeting = f"Hello {name}!"

		await websocket.send(greeting)
		print(f"> {greeting}")

	"""async def handler(self, websocket, path):
		print("a")	
		received = await websocket.recv()
				
				
		print("b")	

		rospy.loginfo('[Websocket API] Received message !')

		sent = '{"status":"failed", "msg":"Data is not JSON"}' #

		try:
			received_json = json.loads(received)
			rospy.loginfo("[Websocket API] Message %s" % str(received_json))
			if set(received_json.keys()) != set(['addon_token', 'action', 'argument']) or received_json['action'] not in ['move','info']:
				sent = '{"status":"failed", "msg":"Invalid request"}'
			elif self.is_authorized_addon(received_json['addon_token']) == False:
				sent = '{"status":"failed", "msg":"Unauthorized Addon token"}'
			elif received_json['action'] == 'move':
				data = received_json['argument']
				if self.is_valid_control_json(data) == False:
					sent = '{"status":"failed", "msg":"Input is not a valid control_json"}'
				else:
					addon = self.client.db.get_addon_by_token(received_json['addon_token'])
					self.client.update_control_json(data)
					self.client.send_goal(addon['name'])
					sent = '{"status":"OK", "msg":"Move goal reached"}'
			else:
				sent = '{"status":"OK", "msg":%s}' % json.dumps(self.client.get_control_json())
		except Exception as e:
			rospy.loginfo("[Websocket API] Error : " + str(e))
			sent = '{"status":"failed", "msg":"Data is not JSON"}

		await websocket.send(sent)
		rospy.loginfo("[Websocket API] Response : %s" % sent)"""

	"""def is_authorized_addon(self, addon_token):
		return self.client.db.is_addon_token_exists(addon_token)"""

	def get_reference_paths(self):
		return list(get_all_paths(self.client.get_control_json()))

	def is_valid_control_json(self, message):
		ref_paths = self.get_reference_paths()
		new_paths = list(get_all_paths(message))
		if set(ref_paths) == set(new_paths):
			return True
		else:
			return False


if __name__ == '__main__':
	try:
		rospy.init_node('websocket_server_node', anonymous=True, disable_signals=True)
		rospy.loginfo("[Websocket API] Starting ...")
		ws = WSServer('0.0.0.0', 8765)		
		asyncio.get_event_loop().run_until_complete(ws.start())
		asyncio.get_event_loop().run_forever()

	except rospy.ROSInterruptException:
		print("Erreur")
