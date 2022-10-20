import socket

srv_addr = input("Enter target IP  : ")
srv_port = input("Enter target port: ")

print(f"Connecting to {srv_addr} on port {srv_port}...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((srv_addr, srv_port))
print("Connected!")

message = input("> ")
s.sendall(message.encode())

s.close()