import cv2
import socket
import pickle
import struct

# Setup the socket for sending video to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'  # Replace with server IP address
port = 9999
client_socket.connect((server_ip, port))

# Initialize camera (this can be a remote camera)
cap = cv2.VideoCapture(1)  # Using the webcam as the client camera

while True:
    success, frame = cap.read()
    if not success:
        break

    # Serialize the frame
    data = pickle.dumps(frame)
    message = struct.pack("Q", len(data)) + data

    # Send to server
    client_socket.sendall(message)

    # Show the client camera feed
    #cv2.imshow('Client - Camera Feed', frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

cap.release()
client_socket.close()
cv2.destroyAllWindows()
