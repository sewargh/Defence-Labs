#!/usr/bin/python3
from scapy.all import *

a = IP()
a.dst = '10.9.0.6'

b = ICMP()

pkt = a/b
send(pkt)
