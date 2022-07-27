import socket
print(socket.gethostbyname(socket.gethostname()))
hostname = socket.gethostname()
print (hostname)
ipaddress= socket.gethostbyname(hostname)
print (ipaddress)