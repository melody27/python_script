#! /usr/bin/env python
from scapy.all import *

        # 实际上此处的 jisuan函数作为prn参数。此处的prn参数实际上是指明回调函数
# 官网demo，简化版arp探测器

def jisuan(pkt):
    if ARP in pkt and pkt[ARP].op == 1:             # 判断是否存在arp包，并且arp包中的op字段为“1”或“2”。
        return pkt.sprintf("{ARP:%ARP.hwsrc% : %ARP.psrc% --> who has %ARP.pdst%}")
    elif ARP in pkt and pkt[ARP].op == 2:
        return pkt.sprintf("{ARP:%ARP.hwsrc% : %ARP.psrc%  say %ARP.pdst%  is at %ARP.hwdst% }")




kkp = sniff(prn=jisuan, filter="arp", store=0)
