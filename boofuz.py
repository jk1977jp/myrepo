#!/usr/bin/python

from boofuzz import *
from string import punctuation



# my boofuzz template. csv logging comes in handy

def main():
	host = "192.168.1.2"
	port = 9999
	
	f = open('boofuzz_log.csv', 'wb')

	session = Session(crash_threshold_request=1,crash_threshold_element=1,fuzz_loggers=[FuzzLoggerCsv(file_handle=f)],
		              receive_data_after_each_request=True,check_data_received_each_request=True,
		              receive_data_after_fuzz=True,
			  target=Target(connection=SocketConnection(host, port, proto='tcp')))
# Define request

	testset = "A"*3 

	s_initialize("Vulnserver")
	s_string("TRUN ", fuzzable=False)
	s_delim(" ",fuzzable=False)
	s_random(punctuation,1,1)
	s_string(testset)
	s_static("\r\n")

# Define Session
	session.connect(s_get("Vulnserver"))

	session.fuzz()

if __name__ == "__main__":
    main()
