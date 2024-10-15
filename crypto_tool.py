import argparse
import os
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

parser = argparse.ArgumentParser(description="Script for encrypting/decrypting a file using Fernet symmetric encryption")

parser.add_argument("target_file", help="The script will target this file and encrypt/decrypt the content")
parser.add_argument("key_file", help="The file which contains the Fernet key that will be used for the encryption/decryption")
parser.add_argument("-e", "--encrypt", action="store_true", help="Set the script to run encryption on the targeted file")
parser.add_argument("-d", "--decrypt", action="store_true", help="Set the script to run decryption on the targeted file")

args = parser.parse_args()


def encrypt_file():
    with open(args.key_file, "rb") as key_file:
        key = key_file.read()
    try:
        fernet_key = Fernet(key)
    except ValueError:
        print("\n*** Error: Invalid Fernet key ***")
        exit()

    if os.path.exists(args.target_file):
        with open(args.target_file, "rb") as file:
            file_data = file.read()

            encrypted_data = fernet_key.encrypt(file_data)

        with open (args.target_file, "wb") as file:
            file.write(encrypted_data)

        print(f"\n*** File successfully encrypted: {args.target_file} ***")

    else:
        print(f"\n*** Target file not found: {args.target_file} ***")


def decrypt_file():
    with open(args.key_file, "rb") as key_file:
        key = key_file.read()
    try:
        fernet_key = Fernet(key)
    except ValueError:
        print("\n*** Invalid Fernet Key ***")
        exit()

    if os.path.exists(args.target_file):
        with open(args.target_file, "rb") as file:
            encrypted_data = file.read()

        try:
            file_data = fernet_key.decrypt(encrypted_data)
            with open (args.target_file, "wb") as file:
                file.write(file_data)
        
            print(f"\n*** File successfully decrypted: {args.target_file} ***")

        except InvalidToken:
            print("\n*** Wrong Fernet key for specified file ***")
            exit()

    else:
        print(f"\n*** Target file not found: {args.target_file} ***")


def main():
    if args.encrypt:
        encrypt_file()

    elif args.decrypt:
        decrypt_file()



if __name__ == "__main__":
    main()
