import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description="Script for sniffing TCP connections in a local network")

parser.add_argument("interface", type=str, help="Interface from which frames will be captured.")

args = parser.parse_args()


def packet_sniffer(packet, log):
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        log.write(f"TCP Connection: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\n")


def main():
    print("*** Packet sniffer started. Monitoring incoming data. Press Ctrl-C to abort ***")
    interface = args.interface
    logfile_name = f"sniffer_{interface}_log.txt"
    with open(logfile_name, 'w') as logfile:
        try:
            sniff(iface=interface, prn=lambda pkt: packet_sniffer(pkt, logfile), store=0)
        except KeyboardInterrupt:
            exit()



if __name__ == "__main__":
    main()
  
