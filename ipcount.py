#!/usr/bin/env python3
#This script is intended to parse a file and provide all IP addresses and how often they populate.
#When using this script, don’t forget to change the log or file and its path.

import pyshark

#Create a variable to open and read the file we are parsing.
cap = pyshark.FileCapture("/home/ozzy/project/project4.pcap")

#Create a dictionary to store all the IPs and counts.
ip_counts = {}

#Loop through each packet in the capture.
for packet in cap:

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

for ip, count in ip_counts.items():

#Print IP addresses and how often they populate.
    print("IP Address:" + (ip) + "  Count:" + (str(count)))

#Pass on any Attribute Errors.





