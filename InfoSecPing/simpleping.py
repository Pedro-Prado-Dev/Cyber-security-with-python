import os

ip_or_host = input("Ping or host for verify: ")
os.system(f'\nping -n 6 {ip_or_host}')