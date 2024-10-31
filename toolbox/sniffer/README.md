# sniffer.py
A simple script for sniffing packets on a local network. Logs the captured data to a .txt file. Written in Python.

## Installation
1. Clone this repo to your local machine:
```
git clone "link"
```
2. Install requirements:
```
pip install -r sniffer_requirements.txt
```
3. Run the script (see usage example)

## Option
**interface** - Network from which frames will be captured. Defaults to monitoring all available networks.

## Usage example
```python
python sniffer.py eth0
```
