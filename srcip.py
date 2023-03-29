#!/usr/bin/env python3

#This script is intended to parse a file to provide the Packet Numbers, Source IPs, and Source Ports.
#When using this script, don't forget to update the log or file and its path.

import pyshark

#Create a variable to open and read the file we are parsing.
cap = pyshark.FileCapture("/home/ozzy/project/project4.pcap")

#Loop through each Packet in the capture.
for packet in cap:
    try:

#Get the Packet Numbers, Source IPs, and Ports.        
        ip_src = packet.ip.src
        tcp_srcport = packet.tcp.srcport
        packet_number = packet.frame_info.number

#Print out the packet numbers with the corresponding IPs and ports.
        print("Packet Number:" + (packet_number) + "  Source IP:" + (ip_src) + "  Source Port:" + (tcp_srcport))

#Pass on any Attribute Errors.    
    except AttributeError:
        pass

