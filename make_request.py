import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.example.com", 80))
s.send(b'GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n')
output = s.recv(4096)
print(output.decode())
s.close()

