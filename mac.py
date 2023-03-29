#! /usr/bin/env python3

#This script is intended to parse a file and provide the Packet Numbers, Source MAC addresses, and Destination MAC addresses.
#When using this script, don't forget to change the log or file and its path.
import pyshark

#Create a variable to open and the the file we need to parse.
cap = pyshark.FileCapture("/home/ozzy/project/project3.pcap")

#Loop through each packet in the capture.
for packet in cap:

#Get the Packet Numbers, Source MACs, and Destination MACs.
    src_mac = packet.eth.src
    dst_mac = packet.eth.dst
    packet_number = packet.frame_info.number

#Print out the Packet numbers with the corresponding Source and Destination MAC addresses.    
    print("Packet Number:" + (packet_number) + "  Source MAC:" + (src_mac) + "  Destination MAC:" + (dst_mac))



