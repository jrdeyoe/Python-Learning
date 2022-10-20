import socket

srv_addr = input("Enter server IP: ")
srv_port = 6666

def print_menu():
    print("""\n\n0) Close Connection
    1) Get system info
    2) List directory contents""")

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect((srv_addr, srv_port))

print(f"Connection established on port {srv_port}!")
print_menu()