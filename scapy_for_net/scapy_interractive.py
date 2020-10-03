import logging

logger = logging.getLogger("scapy")
logger.setLevel(logging.INFO)


from scapy.all import *



class Test(Packet):
    name = "test Packet"

    fields_desc = [
        ShortField("test1",1),
        ShortField("test2",2)
    ]


def make_test(x,y):
    return Ether()/IP(src=get_if_addr(conf.iface),ttl=2)/Test(test1=x,test2=y)

if __name__ == "__main__":
    interact(mydict=globals(),mybanner="this is a test demo")

