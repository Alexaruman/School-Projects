# portscanner.py
A script for scanning IP addresses for open ports using Nmap. Written in Python 3 and designed for penetration testing.

## Installation
1. Clone this repository:

```git clone ""link""```

2. Install requirements:

```pip install -r requirements.txt```

3. Run the script (see example)

## Options
**-ipf, --ip_file** - The script will search this file for IP addresses and scan them.  
**-ip, --ip_list** - Input IP addresses manually for the script to scan. Cannot be used together with the "-ip_file" option.  
**-pr, --port_range** - Set the port range for the scan. Defaults to all ports.  
**-sf, --save_file** - The script will save the results of the scan to this file. If file exists it will append.

## Usage example
```python
python portscanner.py -ipf ip_file.txt -pr 1-10000 -sf scan_result.txt
```
```python
python portscanner.py -ip 127.0.0.1 127.0.0.2 -sf scan_result.txt
```
