import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        print(f'\nIp verificado: {ip}')
        os.system(f'ping -n 2 {ip}')
        time.sleep(3)