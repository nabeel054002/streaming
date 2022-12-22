# Welcome to PyShine
# In this video server is receiving video from clients.
# Lets import the libraries
import socket, cv2, pickle, struct
import imutils
import threading
import pyshine as ps # pip install pyshine
import cv2
import numpy as np
import time

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP="127.0.0.1"
PORT=12345
socket_address=(IP,PORT)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at",socket_address)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps=30
size=(640,480)
writer = cv2.VideoWriter("output.mp4", fourcc, fps, size)
def pil_to_cv(pil_image):
    """
    Returns a copy of an image in a representation suited for OpenCV
    :param pil_image: PIL.Image object
    :return: Numpy array compatible with OpenCV
    """
    return np.array(pil_image)[:, :, ::-1]
def show_client(addr,client_socket):
    try:
        print('CLIENT {} CONNECTED!'.format(addr))
        if client_socket: # if a client socket exists
            data = b""
            payload_size = struct.calcsize("Q")
            while True:
                while len(data) < payload_size:
                    packet = client_socket.recv(4*1024)
                    if not packet: break
                    data+=packet
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q",packed_msg_size)[0]

                while len(data) < msg_size:
                    data += client_socket.recv(4*1024)
                frame_data = data[:msg_size]
                data  = data[msg_size:]
                frame = pickle.loads(frame_data)
                text  =  f"CLIENT: {addr}"
                frame =  ps.putBText(frame,text,10,10,vspace=10,hspace=1,font_scale=0.7, background_RGB=(255,0,0),text_RGB=(255,250,250))
                writer.write(pil_to_cv(frame))
                cv2.imshow(f"FROM\{addr}",frame)
                key = cv2.waitKey(1)
                if key  == ord('q'):
                    break
        writer.release()
        client_socket.close()
    except Exception as e:
        print(f"CLIENT {addr} DISCONNECTED")
        pass

while True:
    client_socket,addr = server_socket.accept()
    thread = threading.Thread(target=show_client, args=(addr,client_socket))
    thread.start()
    print("TOTAL CLIENTS ",threading.activeCount() - 1)


# # Welcome to PyShine
# # In this video server is receiving video from clients.
# # Lets import the libraries
# import socket, cv2, pickle, struct
# import imutils
# import threading
# import pyshine as ps # pip install pyshine
# import cv2
# import time

# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# IP="127.0.0.1"
# PORT=12345
# socket_address=(IP,PORT)
# server_socket.bind(socket_address)
# server_socket.listen()
# print("Listening at",socket_address)
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# fps=30
# size=(640,480)
# output_file="output.avi"
# out = cv2.VideoWriter(output_file, fourcc, fps, size, True)

# def show_client(addr,client_socket):
#     try:
#         print('CLIENT {} CONNECTED!'.format(addr))
#         if client_socket: # if a client socket exists
#             data = b""
#             payload_size = struct.calcsize("Q")
#             while True:
#                 while len(data) < payload_size:
#                     packet = client_socket.recv(4*1024)
#                     if not packet: break
#                     data+=packet
#                 packed_msg_size = data[:payload_size]
#                 data = data[payload_size:]
#                 msg_size = struct.unpack("Q",packed_msg_size)[0]

#                 while len(data) < msg_size:
#                     data += client_socket.recv(4*1024)
#                 frame_data = data[:msg_size]
#                 data  = data[msg_size:]
#                 frame = pickle.loads(frame_data)
#                 text  =  f"CLIENT: {addr}"
#                 frame =  ps.putBText(frame,text,10,10,vspace=10,hspace=1,font_scale=0.7, background_RGB=(255,0,0),text_RGB=(255,250,250))
# 			    out.write(frame)
#                 cv2.imshow(f"FROM\{addr}",frame)
#                 key = cv2.waitKey(1)
#                 if key  == ord('q'):
#                     break
#             out.release()
#         client_socket.close()
#     except Exception as e:
#         print(f"CLIENT {addr} DISCONNECTED")
#         pass

# while True:
#     client_socket,addr = server_socket.accept()
#     thread = threading.Thread(target=show_client, args=(addr,client_socket))
#     thread.start()
#     print("TOTAL CLIENTS ",threading.activeCount() - 1)

	
				



# # Welcome to PyShine
# # In this video server is receiving video from clients.
# # Lets import the libraries
# import socket, cv2, pickle, struct
# import imutils
# import threading
# import pyshine as ps # pip install pyshine
# import cv2
# import time

# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# IP="127.0.0.1"
# PORT=12345
# socket_address=(IP,PORT)
# server_socket.bind(socket_address)
# server_socket.listen()
# print("Listening at",socket_address)

# fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Choose a codec
# fps = 30 # Set the frame rate
# size = (640, 480) # Set the frame size
# output_file = "output.avi" # Set the output file name
# out = cv2.VideoWriter(output_file, fourcc, fps, size)

# def show_client(addr,client_socket):
# 	try:
# 		print('CLIENT {} CONNECTED!'.format(addr))
# 		if client_socket: # if a client socket exists
# 			data = b""
# 			payload_size = struct.calcsize("Q")
# 			while True:
# 				while len(data) < payload_size:
# 					packet = client_socket.recv(4*1024)
# 					if not packet: break
# 					data+=packet
# 				packed_msg_size = data[:payload_size]
# 				data = data[payload_size:]
# 				msg_size = struct.unpack("Q",packed_msg_size)[0]
# 				#print(data)
# 				while len(data) < msg_size:
# 					data += client_socket.recv(4*1024)
# 				frame_data = data[:msg_size]
# 				data  = data[msg_size:]
# 				frame = pickle.loads(frame_data)
# 				text  =  f"CLIENT: {addr}"
# 				frame =  ps.putBText(frame,text,10,10,vspace=10,hspace=1,font_scale=0.7, background_RGB=(255,0,0),text_RGB=(255,250,250))
#                 cv2.imshow(f"FROM {addr}",frame)
# 				key = cv2.waitKey(1) & 0xFF
# 				if key  == ord('q'):
# 					break
# 			client_socket.close()
# 	except Exception as e:
# 		print(f"CLINET {addr} DISCONNECTED")
# 		pass
		
# while True:
# 	client_socket,addr = server_socket.accept()
# 	thread = threading.Thread(target=show_client, args=(addr,client_socket))
# 	thread.start()
# 	print("TOTAL CLIENTS ",threading.activeCount() - 1)
	
				

