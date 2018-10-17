from scapy.all import *
import pprint

'''

this script was written while doing exercises from "Network Forensics: Tracking Hackers through Cyberspace"
quick, darty but do the job...
'''


data = "evidence-packet-analysis.pcap"
a = rdpcap(data)

sessions = a.sessions()

txt = ""
for session in sessions:
	for pkt in sessions[session]:
		try:
			if pkt[TCP].dport == 143 or pkt[TCP].sport == 143:
				li= str(pkt[TCP].payload[Raw].load).lstrip("b").replace("\\r\\n","\n").replace("\'","").replace("\\t","	")
				txt += li
				
		except:
			pass

print(txt)
