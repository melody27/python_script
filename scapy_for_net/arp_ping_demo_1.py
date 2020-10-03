import sys

# this is a arp scan demo

if not sys.argv[1]:
    pass
    print("please entry the net scope to arp ping ")
    print("\x33[91m1")
    exit()

from scapy.all import *

conf.verb = 0
ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1],op=1),timeout=2)


for snd, rcv in ans:
    print(rcv.sprintf("{ARP: %ARP.hwsrc% --> %ARP.psrc%}"))


# import sys

# from scapy.all import srp,Ether,ARP,conf
# conf.verb=0
# ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),
#               timeout=2)


# for snd,rcv in ans:
#     print(rcv.sprintf(r"%Ether.src% & %ARP.psrc%"))
