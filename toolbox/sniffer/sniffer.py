import argparse
import datetime
from scapy.all import *

parser = argparse.ArgumentParser(description="Script for sniffing TCP connections in a local network")
parser.add_argument("-i", "--interface", type=str, help="Network from which frames will be captured. Defaults to monitoring all available networks")
args = parser.parse_args()


def packet_sniffer(packet, savefile):
    print(f"[{datetime.now()}] - {packet.summary()}")
    with open(savefile, 'a') as file:
        file.write(f"[{datetime.now()}] - {packet.summary()}\n")


def main():
    print("*** Packet sniffer started. Monitoring incoming data. Press Ctrl-C to abort ***")

    if args.interface:
        interface = args.interface
        savefile = f"sniffer_{interface}_log.txt"
        sniff(iface=interface, prn=lambda packet: packet_sniffer(packet, savefile), store=0)
    else:
        savefile = "sniffer_log.txt"
        sniff(prn=lambda packet: packet_sniffer(packet, savefile), store=0)



if __name__ == "__main__":
    main()
