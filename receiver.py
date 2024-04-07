import scapy.all as scapy

def handle_packet(packet):
    if scapy.ICMP in packet:
        icmp_packet = packet[scapy.ICMP]
        print(f"payload = {icmp_packet.payload.load}")
scapy.sniff(filter="icmp", prn=handle_packet)