import socket

target = input("Enter Target IP: ")
port_range = input("Enter Port Range (ex 5-200): ")

lowport = int(port_range.split('-')[0])
highport = int(port_range.split('-')[1])

print(f"Scanning host {target} from port {lowport} to {highport}...")

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print(f"*** Port {port} - OPEN ***")
    else:
        print(f"Port {port} - CLOSED!")
    s.close()