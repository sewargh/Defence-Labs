#!/usr/bin/python3
from scapy.all import *

def print_pkt(pkt):
	pkt.show()

#filter1
pkt = sniff(iface = 'br-acd6f53cd73f', filter='icmp', prn=print_pkt)

#filter2
#pkt = sniff(iface = 'br-acd6f53cd73f', filter='tcp and src host 10.9.0.5 and dst port 23', prn=print_pkt)

#filter3
#pkt = sniff(iface = 'br-acd6f53cd73f', filter='net 129.230.0.0/16', prn=print_pk)
