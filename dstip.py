#!/usr/bin/env python3

#This script is intended to parse a file to provide the Packet numbers, Destination IPs, and Destination Ports.
#When using this script, don't forget to change to the log or file and its path.

import pyshark

#Create a variable to open and read the file we need to parse.
cap = pyshark.FileCapture("/home/ozzy/project/project4.pcap")

#Loop through each packet in the capture.
for packet in cap:
    try:

#Get the Packet Numbers, Destination IPs, and Destination Ports.
        ip_dst = packet.ip.dst
        tcp_dstport = packet.tcp.dstport
        packet_number = packet.frame_info.number
        
#Print out the Packet Numbers with the corresponding IPs and Ports.
        print("Packet Number:" + (packet_number) + "  Destination IP:" + (ip_dst) + "  Destination Port:" + (tcp_dstport))
    
#Pass on any Attribute Errors.
    except AttributeError:
        pass


