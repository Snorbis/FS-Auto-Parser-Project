#! /usr/bin/env python3

#This script is intended to parse a file and provide the Packet Numbers, and their Timestamps.
#When using this script, don’t forget to change the log or file and its path.

import pyshark

#Create a variable to open and read the file we are parsing.
cap = pyshark.FileCapture("/home/ozzy/project/project4.pcap")

#Loop through each packet in the capture.
for packet in cap:

#Get Packet Numbers and their Timestamps.
    timestamp = packet.sniff_time
    packet_number = packet.frame_info.number

#Print out the Packet Numbers and their Timestamps.
    print("Packet Number:" + (packet_number) + "  Timestamp:" + (str(timestamp)))






