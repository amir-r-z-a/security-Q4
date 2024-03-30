import scapy.all as scapy
def handle_packet(packet):
    if scapy.ICMP in packet:
        icmp_packet = packet[scapy.ICMP]
        # Decode and process the ICMP packet here
        # For example, you can print the packet summary
        print(icmp_packet.payload.load)

# Set up the packet capture and filter ICMP packets
scapy.sniff(filter="icmp", prn=handle_packet)

# import sys
# print(sys.path)