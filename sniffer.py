#!/usr/bin/python3
from scapy.all import *

def print_pkt(pkt):
	pkt.show()

pkt = sniff(iface = 'br-acd6f53cd73f', filter='icmp', prn=print_pkt)
