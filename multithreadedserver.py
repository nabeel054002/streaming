import socket 
import threading 

IP="192.168.0.156"
PORT=12345
ADDR=(IP,PORT)
SIZE=1024
FORMAT="utf-8"
DISCONNECT_MSG="DISCONNECT"

def handle_client(conn, addr):
    print(f'New connection at address, {addr}')
    connected=True
    while connected: 
        msg =conn.recv(SIZE).decode(FORMAT)
        if msg==DISCONNECT_MSG:
            connected=False 
        print(f'{addr} is current address, sending message = {msg}')
        #some extra string added in the start to msg 
        msg = f"Msg recieved: {msg}"
        conn.send(msg.encode(FORMAT))
    conn.close()

def main(): 
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#sock_stream is for tcp protocol
    print(ADDR)
    server.bind(ADDR)
    server.listen()
    print(f'Server is listening on {IP}, {PORT}')

    while True: 
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'Active connections are {threading.active_count()-1}')

if __name__=="__main__":
    main()