import socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.156', 12345))
server_socket.listen(5)
#does this mean to listen to 5 diffnt clients at max ?
while True: 
    print('Server waiting for communication')
    client_socket, addr = server_socket.accept()
    print(client_socket, type(client_socket))
    print('client connected from ', addr)
    while True: 
        data = client_socket.recv(1024)
        #1024 bits of info to be recieved? 
        if not data or data.decode('utf-8')=='END':
            break 
        print(f'recieved from client client: {data.decode("utf-8")}')
        try: 
            client_socket.send(bytes("Hey client", "utf-8"))
        except: 
            print("Exited by user")
    client_socket.close()
    server_socket.close() 
    