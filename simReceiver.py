import threading
import socketserver
import json
from log_file import CsvFile

class UDPRequestHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request[0]  ##UDP requests come with a string [0] and a socket [1]
		if data:
			package = json.loads(data)
			#We should now have a python Dict of name/value pairs.
			#Turn it into a line of CSV data the most Pythonic way (see log_file.py)
			self.server.scenario.addLogLine(CsvFile.fromDict(package))			 
			
		
class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
	pass

class SimReceiver:

	def __init__(self, scenario):
		ip="localhost"
		port=4000
		server = ThreadedUDPServer((ip, port), UDPRequestHandler)
		server.scenario = scenario
		server_thread = threading.Thread(target=server.serve_forever)
		server_thread.daemon = True
		server_thread.start()
	
	def __del__(self):
		server.shutdown()