# sniffer.py
A simple script for sniffing packets on a local network using scapy. Logs the captured data to a .txt file. Written in Python.

## Installation
1. Clone this repo to your local machine:
```
git clone https://github.com/Alexaruman/School-Projects.git
```
2. Install requirements:
```
pip install -r sniffer_requirements.txt
```
3. Run the script (see usage example)

## Arguments and options
**interface** - Network from which frames will be captured. Defaults to monitoring all available networks.

## Usage example
```python
python sniffer.py eth0
```
