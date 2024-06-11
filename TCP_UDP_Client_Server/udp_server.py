import socket


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print('Socket run')


host = 'localhost'
port = 5432

s.bind((host, port))
msg = 'Server: Hello client!!'


while 1:
    data, end = s.recvfrom(4096)

    if data:
        print(f'Server invite message')
        s.sendto(data + (msg.encode()), end)