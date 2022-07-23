#!/usr/bin/python3
from scapy.all import *

a = IP()
a.dst = '10.0.2.4'
a.src = '1.2.3.4'

b = ICMP()

pkt = a/b
send(pkt)
