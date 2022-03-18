from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re 
import socket 
from threading import Thread

import requests
from urllib.parse import urljoin
from faker import Faker
import responses
from django.conf import settings

fake = Faker()

base_actionnetwork_API_URL = "https://actionnetwork.org/api/v1"

@responses.activate
def initiate_mock_actionnetwork(faker):
	mock_get_user_endpoint = urljoin(base_actionnetwork_API_URL, "people")
	mock_user_email = faker.email()
	responses.add(responses.GET, mock_get_user_endpoint)


def call_mock_api(URI, params=None):
    return requests.get(
        URI,
        params=params,
        headers={"OSDI-API-Token": settings.ACTIONNETWORK_API_KEYS["main"]},
    ).json()

class MockServerRequestHandler(BaseHTTPRequestHandler):	
	CAMPAIGNS_PATTERN = re.compile(r'/campaigns')
	EVENTS_PATTERN = re.compile(r'/events')
	PEOPLE_PATTERN = re.compile(r'/people')

	def do_GET(self):
    	# GET /people
		if re.search(self.PEOPLE_PATTERN, self.path):
			# Add response status code
			self.send_response(requests.code.ok)

			# Add response headers
			self.send_header('Content-Type', 'application/json; charset=utf-8')
			self.end_headers()

			# Add response content
			response_content = json.dumps([])
			self.wfile.write(response_content.encode('utf-8'))
			return
		# GET /events
		elif re.search(self.EVENTS_PATTERN, self.path):
			# Response status code
			# TODO
			return

	def do_POST(self):
		#TODO
		return

def get_free_port():
	s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
	s.bind(('localhost', 0))
	address, port = s.getsockname()
	s.close()
	return port


def start_mock_server(port):
	mock_server = HTTPServer(('localhost', port), MockServerRequestHandler)
	mock_server_thread = Thread(target=mock_server.serve_forever)
	mock_server_thread.setDaemon(True)
	mock_server_thread.start()