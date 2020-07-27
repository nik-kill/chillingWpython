#!usr/bin/env python

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet())
queue.run()

# iptables -I FORWARD -j NFQUEUE --queue-num 0
#   when man in middle
#       FORWARD
#   when on same system
#       OUTPUT
#       INPUT

# iptables --flush
#to clear iptable

# echo 1 > /proc/sys/net/ipv4/ip_forward
