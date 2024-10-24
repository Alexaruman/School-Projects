# crypto_tool.py
A simple script for encrypting / decrypting the contents of a file using Fernet symmetric encryption. Written in Python 3.

## Installation
1. Clone this repo to your local machine:
```
git clone https://github.com/Alexaruman/School-Projects.git
```
2. Install requirements:
```
pip install -r crypto_requirements.txt
```
3. Run the script (see usage example)

## Arguments
**target_file** - The script will target this file and encrypt / decrypt the content  
**key_file** - The file which contains the Fernet key that will be used for the encryption / decryption

## Options
**-e, --encrypt** - Set the script to run encryption on the target_file  
**-d, --decrypt** - Set the script to run decryption on the target_file  
**-h, --help** - Show help message and exit

## Usage example
```python
python crypto_tool.py -e crypto_test_file.txt key_file.key
```

# generate_key.py
A simple script that generates and saves a Fernet encryption key to a file.

## Installation
1. Clone this repo to your local machine:
```
git clone https://github.com/Alexaruman/School-Projects.git
```
2. Install requirements:
```
pip install -r crypto_requirements.txt
```
3. Run the script (see usage example)

## Arguments and options
**filename** - Name of the file that will be created for the Fernet key  
**-h, --help** - Show help message and exit

## Usage example
```python
python generate_key.py key_file.key
```
