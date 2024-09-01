#!/usr/bin/env python3


#Import Scapy
from scapy.all import *
import argparse


L2Broadcast = "FF:FF:FF:FF:FF:FF"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", type=str, dest="target", required=True, help="Choose target IP or IP Range")
    parser.add_argument("-i", type=str, dest="interface", required=True, help="Choose your interface")
    args = parser.parse_args()

    return args


def arpscan(target,interface):
    frame = Ether(dst=L2Broadcast, type=0x0806)
    frame /= ARP(pdst=args.target)
    answered_list = srp(frame, iface=args.interface, timeout=1, verbose=0)[0]
    for send,recive in answered_list:
        print (recive.sprintf(r"%Ether.src% - %ARP.psrc%"))
    


args = get_arguments()
arpscan(args.target, args.interface)
