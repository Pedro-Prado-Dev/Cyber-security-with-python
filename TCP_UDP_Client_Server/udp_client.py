import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM = UDP

print('Socket client run')

host = 'localhost'
port = 5433
msg = 'Hello Word!'

try:
    s.sendto(msg.encode(), (host, 5432))
    
    data, servidor = s.recvfrom(4096)
    data = data.decode()
    
    print(f'Client: {data}')

finally:
    print('Client closed the connection')
    s.close()