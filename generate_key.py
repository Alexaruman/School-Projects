import argparse
import os
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description="A simple script that generates and saves a Fernet key to a file")

parser.add_argument("filename", help="Name of the file that will be created for the Fernet key")

args = parser.parse_args()


def generate_key():
    if not os.path.exists(args.filename):
        with open(args.filename, "wb") as file:
            key = Fernet.generate_key()
            print("*** Key generated ***")
            file.write(key)
            print(f"Key was saved to file: {args.filename}")
    else:
        print(f"\n*** File already exists: {args.filename} ***")



if __name__ == "__main__":
    generate_key()
