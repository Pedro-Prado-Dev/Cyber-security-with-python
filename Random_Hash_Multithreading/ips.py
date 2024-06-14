import ipaddress

ip = '192.168.0.0/24'

network = ipaddress.ip_network(ip, strict=False)

for ip in network:
    print(ip)