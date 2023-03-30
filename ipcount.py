#!/usr/bin/env python3
#This script is intended to parse a file and provide all IP addresses and how often they populate.
#When using this script, don’t forget to change the log or file and its path.

import pyshark

#Create a variable to open and read the file we are parsing.
cap = pyshark.FileCapture("/home/ozzy/project/project2.pcap")

#Create a dictionary to store all the IPs and counts.
ip_counts = {}

#Loop through each packet in the capture.
for packet in cap:
    try:

#Get the Source IPs and Destiantion IPs.
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst

#Increment the count for the source IP addresses.
        if ip_src not in ip_counts:
            ip_counts[ip_src] = 1
        else:
            ip_counts[ip_src] += 1
    
#Increment the count for the destination IP addresses.
        if ip_dst not in ip_counts:
            ip_counts[ip_dst] = 1
        else:
            ip_counts[ip_dst] += 1

#Pass on any Attribute Errors.
    except AttributeError:
        pass
#Print IP addresses and how often they populate.
for ip, count in ip_counts.items():
   print("IP Address:" + (ip) + "  Count:" + (str(count)))






