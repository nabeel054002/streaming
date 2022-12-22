import sys#to do appropo err handling
import socket 

try:
    s=socket.socket(family=AF_INET, type=SOCK_STREAM, port=0)
    #type defines if it is tcp or udp 
except socket.error as err:
    print("Failed to create a network")
    print("Reason",str(err))

    sys.exit()
print("socket created")

target_host = input("Enter target_host to whom mwe should connect to")
target_port = input("Enter the input port ")

try:
    sock.connect(target_host, int(target_port))
    print(f'Socket connected to {target_host} on port {target_port}')
    sock.shutdown(2)#what is this line
except socket.error as err:
    print("Failed to connect since", err)
    sys.exit()