import socket, platform, os

srv_addr = ""
srv_port = 6666

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySock.bind((srv_addr, srv_port))
mySock.listen(1)

connection, address = mySock.accept()

while 1:
    try:
        data = connection.recv(1024)
    except:continue

    if(data.decode('utf-8') == '1'):
        toSend = platform.platform() + " " + platform.machine()
        connection.sendall(toSend.encode())

    elif(data.decode('utf-8') == '2'):
        data = connection.recv(1024)
        try:
            fileList = os.listdir(data.decode('utf-8'))
            toSend = ""
            for file in fileList:
                toSend += "," + file
        except:
            toSend = "Wrong path!"
            connection.sendall(toSend.encode())

    elif(data.decode('utf-8') == '0'):
        connection.close()
        connection, address = mySock.accept()