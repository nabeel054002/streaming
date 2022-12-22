import socket, pickle, struct, cv2
import pyshine as ps#optional module
import imutils

camera = True 
if camera==True: 
    vid = cv2.VideoCapture(0)
else:
    vid = cv2.VideoCapture('videos/random.mp4')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP="127.0.0.1"
PORT=12345
ADDR=(IP,PORT)
client_socket.connect(ADDR)
if client_socket: 
    while(vid.isOpened()):
        try:
            img, frame = vid.read()
            frame = imutils.resize(frame,width=380)
            a = pickle.dumps(frame)#to convert the vid into bytes
            message = struct.pack("Q",len(a))+a#the bytes are then packed into q format to generate 
            #the msg
            client_socket.sendall(message)
            cv2.imshow(f"TO: {IP}",frame)#how can i view the frames
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                client_socket.close()
        except:
            print("VIDEO FINISHED")
            break