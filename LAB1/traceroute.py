#!/usr/bin/python3
from scapy.all import *

ip = IP()
icmp = ICMP()
ip.dst = '10.9.0.10'
TTL = 1

print ("************** TraceRoute to IP ", ip.dst, " **************")
while True and TTL <= 255:

	ip.ttl = TTL
	pkt = ip/icmp 
	replyPkt = sr1(pkt, verbose =0, timeout = 2)
	if replyPkt == None:
		print(str(TTL)+") IP: ***", )
		
	elif replyPkt[ICMP].type == 11:
		print(str(TTL)+") IP:", replyPkt[IP].src)

	else:
		break

	TTL += 1
	pkt.ttl = TTL

print(str(TTL)+") IP:", replyPkt[IP].src)
