import socket

srv_addr = input("IP Address : ")
srv_port = input("Server port: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((srv_addr, srv_port))
s.listen(1)
print("Started... waiting for connections...")

connection, address = s.accept()
print("Client connected: ", address)

while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))

connection.close()

