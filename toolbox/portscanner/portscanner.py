import nmap
import os
import re
import pprint
import argparse

parser = argparse.ArgumentParser(description="Script for scanning IP addresses with Nmap")

parser.add_argument("-ipf", "--ip_file", nargs="?", help="Script will search this file for IP addresses and scan them")
parser.add_argument("-ip", "--ip_list", nargs="+", help="Input IP addresses manually and the script will scan them")
parser.add_argument("-pr", "--port_range", nargs="?", const="1-65535", default="1-65535", help="Set the port range for the scan. Defaults to all ports")
parser.add_argument("-sf", "--save_file", nargs="?", help="Script will save scan results to this file. If file exists it will append")

args = parser.parse_args()

nm = nmap.PortScanner()


def scan(hosts, port_range):
    result = []
    for host in hosts:
        nm.scan(host, arguments = f"-p{port_range}")
        result.append(nm[host])
        print("********************************")
        print("Host : %s (%s)" % (host, nm[host].hostname()))
        print("State : %s" % nm[host].state())
            
        for proto in nm[host].all_protocols():
            print("***********")
            print("Protocol : %s" % proto)
            lport = nm[host][proto].keys()
            sorted(lport)
                
            for port in lport:
                print ("port : %s\tstate : %s\tservice : %s" % (port, nm[host][proto][port]['state'], nm[host][proto][port]['name']))
            
        print ("********************************")
    return result


def scan_import():
    if os.path.exists(args.ip_file):
        with open(args.ip_file, 'r') as file:
            lines = file.readlines()
            pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})") 
            hosts = []
                
            for line in lines:
                match = pattern.findall(line)
                if len(match) != 0:    
                    hosts.append(match[0])

            if len(hosts) != 0:
                print(f"\n{len(hosts)} valid targets accepted. Starting scan...\n")
                result = scan(hosts, args.port_range)
                return result

            else:
                print(f"No valid targets found in file: {args.ip_file}")
                exit()

    else:
        print(f"File not found: {args.ip_file}")
        exit()


def save_to_file (scan_result):
    if not os.path.exists(args.save_file):
        with open(args.save_file, 'w') as output_file:
            for result in scan_result:
                pprint.pprint(result, output_file)
            print(f"Created file and added scan result: {args.save_file}")

    else:
        with open(args.save_file, 'a') as output_file:
            for result in scan_result:
                pprint.pprint(result, output_file)
            print(f"Added scan result to file: {args.save_file}")



def main():
    if args.ip_file == None:
        hosts = []
        pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

        for host in args.ip_list:
            if pattern.match(host):
                hosts.append(host)

        if len(hosts) != 0:
            print(f"\n{len(hosts)} valid targets accepted. Starting scan...\n")
            result = scan(hosts, args.port_range)
            print("\n*** Scan complete ***\n")
            if args.save_file != None:
                save_to_file(result)

        else:
            print("\nNo valid IP addresses to scan. Exiting ...\n")

    elif args.ip_file:
        result = scan_import()
        print("\n*** Scan complete ***\n")
        if args.save_file != None:
            save_to_file(result)



if __name__ == "__main__":
    main()
    
