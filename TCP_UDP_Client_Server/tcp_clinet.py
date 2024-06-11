import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # AF_INET = IP protocol     SOCK_STREAM = TCP protocol    0 = protocol for comunication to server (TCP)
    except socket.error as e:
        print(f'Connection Falied')
        print(f'Error :{e}')
        sys.exit()
        
    print('Socket run')
    
    
    host = input('Host ro connect: ')
    port = input('Port to connect: ')
    
    try:
        s.connect((host, int(port)))
        print(f'TCP Client connected successfully host: {host} on port: {port}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Connection Falied')
        print(f'Error :{e}')
        sys.exit()

if __name__ == '__main__':
    main()