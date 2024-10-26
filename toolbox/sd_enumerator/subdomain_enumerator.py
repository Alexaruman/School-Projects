import sublist3r
import requests
import argparse

parser = argparse.ArgumentParser(description="Script for enumerating subdomains using the sublist3r and requests libraries.")

parser.add_argument("domain", help="The domain which the script will list subdomains for")

args = parser.parse_args()


def sd_enumerator(domain, savefile):
    subdomains = sublist3r.main(domain, 20, savefile = None, ports = None, silent = True, verbose = False, enable_bruteforce = False, engines = None)
    savefile = f"{domain}_subdomains.txt"

    with open(savefile, "w") as file:
        file.write(f"*** Domain: {domain} ***\n")
        for subdomain in subdomains:
            try:
                response = requests.get(f"https://{subdomain}", timeout = 5)
                status = response.status_code
                print(f"Subdomain is UP: {subdomain} --- Status code: {status}")
                file.write(f"Subdomain is UP: {subdomain} --- Status code: {status}\n")
            except requests.ConnectionError:
                print(f"Subdomain is DOWN: {subdomain}")
                file.write(f"Subdomain is DOWN: {subdomain}\n")
            except requests.Timeout:
                print(f"Subdomain timed out: {subdomain}")
                file.write(f"Subdomain timed out: {subdomain}\n")

    print(f"*** Enumeration done. Saved results to file: {savefile} ***")


def main():
    domain = args.domain
    savefile = f"{domain}_subdomains.txt"
    sd_enumerator(domain, savefile)



if __name__ == "__main__":
    main()
