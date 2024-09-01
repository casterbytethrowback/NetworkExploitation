# NetworkExploitation

This repository stores tools for conducting network attacks. 

**The author has nothing to do with those who will use these tools for personal purposes to destroy other people's computer networks. The tools are presented for training purposes to help engineers improve the security of their network.**

The repository was created on January 8, 2022. Over time, this repository will be updated and filled with more tools.

Please, read the source code of these scripts before using these tools. 

**You need to know what you're doing.** **Don't be like a script-kiddie!**

**ᛝ** 

-----------------------------------------------------------------------------------------------------------------------------------------
**ARPScanner.py** - This scanner is designed to detect "live" hosts on the network. ARP scanning is quite noisy, keep in mind.

**ARPSpoofer.py** - This tool is designed to carry out an ARP-Spoofing attack. It also has the function of restoring ARP tables. And this tool is fully parameterized. Specify the victim's address, gateway and network interface.

**DHCPAbuse.py** - This tool is designed for the abuse of a DHCP server (DHCP Starvation Attack)

**DTPAbuse.py** - This tool is designed to carry out a "VLAN Hopping" attack using the shortcomings of the DTP protocol (Dynamic Trunking Protocol)

**DoSNetwork.py** - This tool generates random MAC addresses and generates random IP packets with subsequent ICMP sending. Running this script may cause the local network to crash. I believe that this script can serve as a kind of "stress test" for your network.

**HSRPHijacking.py** - This tool is designed to attack the HSRP (Hot Standby Redundancy protocol) Become the main router!

**MACFlooder.py** - This tool is designed for abusing the switch table. (CAM Table Overflow Attack)

**STPRootAttack.py** - This tool designed to attack the STP protocol (802.1D). The script will send malicious BPDUs, which will eventually make you a root switch.

**TCPSYNFlooding.py** - This script is designed to carry out a TCP-SYN Flooding attack. The script initiates sending a huge number of TCP SYN segments.

**VRRPSpoofing.py** - This tool is designed to attack the VRRP (Virtual Router Redundancy Protocol) protocol. With this script, you will become the **master VRRP router**. But keep in mind that this script will work if VRRP is configured on the target routers without any authentication. In the future, the script will be updated, you will be able to specify these authentication strings.


