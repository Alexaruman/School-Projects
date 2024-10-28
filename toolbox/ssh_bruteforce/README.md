# ssh_bruteforce.py
Script for bruteforcing an SSH login using paramiko. Written in Python.

## Installation
1. Clone this repo to your local machine:
```
git clone "link"
```
2. Install requirements:
```
pip install -r ssh_requirements.txt
```
3. Run the script (see usage example)

## Arguments
**username_file** - The script will attempt a login with each line in this file as a username  
**password_file** - The script will attempt a login with each line in this file as a password

## Options
**-s**, **--sleep** - Optional wait time between attempted logins. Input in seconds (ex- 1, 0.1)

## Usage example
```python
python ssh_bruteforce.py 127.0.0.1 usernames.txt passwords.txt -s 0.1
```
