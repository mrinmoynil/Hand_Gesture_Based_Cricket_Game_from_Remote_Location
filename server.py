# import cv2
# import socket
# import pickle
# import struct
# import mediapipe as mp
# import time

# # Initialize MediaPipe and socket
# mp_hands = mp.solutions.hands
# mp_draw = mp.solutions.drawing_utils
# hands = mp_hands.Hands()

# # Initialize socket for client-server communication
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 9999))
# server_socket.listen(1)
# print('Waiting for client connection...')
# client_socket, addr = server_socket.accept()
# print('Client connected:', addr)

# # Load the background image
# background_image = cv2.imread('score.jpg')

# # Open the server's camera feed
# cap = cv2.VideoCapture(0)

# # Variables for tracking iteration, points, and phase
# iteration_count = 1
# max_iterations = 12
# server_points = 0
# client_points = 0
# is_server_turn = True  # First 6 for server, next 6 for client

# def detect_fingers(image):
#     """Detect fingers and draw landmarks, returning finger array."""
#     finger_array = [0, 0, 0, 0, 0]
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     result = hands.process(image_rgb)
    
#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             landmarks = hand_landmarks.landmark
#             tolerance = 0.005

#             # Detect each finger state
#             thumb_tip, thumb_ip = landmarks[4], landmarks[3]
#             index_tip, index_dip = landmarks[8], landmarks[7]
#             middle_tip, middle_dip = landmarks[12], landmarks[11]
#             ring_tip, ring_dip = landmarks[16], landmarks[15]
#             pinky_tip, pinky_dip = landmarks[20], landmarks[19]
            
#             finger_array[0] = 1 if thumb_tip.x < thumb_ip.x - tolerance else 0
#             finger_array[1] = 1 if index_tip.y < index_dip.y - tolerance else 0
#             finger_array[2] = 1 if middle_tip.y < middle_dip.y - tolerance else 0
#             finger_array[3] = 1 if ring_tip.y < ring_dip.y - tolerance else 0
#             finger_array[4] = 1 if pinky_tip.y < pinky_dip.y - tolerance else 0

#     return finger_array, image

# while True:
#     # Capture server camera frame
#     success, server_frame = cap.read()
#     if not success:
#         break
    
#     # Resize and set up background
#     server_frame_resized = cv2.resize(cv2.flip(server_frame, 1), (450, 654))
#     background_copy = background_image.copy()
#     background_copy[0:654, 0:450] = server_frame_resized

#     # Receive and process client frame
#     client_frame_data = client_socket.recv(4096)
#     if not client_frame_data:
#         break
#     client_frame = pickle.loads(client_frame_data)
#     client_frame_resized = cv2.resize(cv2.flip(client_frame, 1), (450, 654))
#     background_copy[0:654, 550:1000] = client_frame_resized

#     # Detect fingers for server and client
#     server_fingers, server_frame_with_landmarks = detect_fingers(server_frame_resized)
#     client_fingers, client_frame_with_landmarks = detect_fingers(client_frame_resized)

#     # Display server and client fingers array on screen
#     cv2.putText(background_copy, f"Server Fingers: {server_fingers}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(background_copy, f"Client Fingers: {client_fingers}", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
#     #printing arrays
#     print(server_fingers)
#     print(client_fingers)
    
    
#     # Points update logic
#     if is_server_turn:
#         if server_fingers != client_fingers:
#             server_points += sum(server_fingers)
#     else:
#         if server_fingers != client_fingers:
#             client_points += sum(client_fingers)

#     print(server_points)
#     print(client_points)

#     # Show current points
#     cv2.putText(background_copy, f"Server Points: {server_points}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(background_copy, f"Client Points: {client_points}", (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     # Display iteration
#     cv2.putText(background_copy, f"Iteration: {iteration_count}", (420, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 6)

#     # Update iteration count and switch turn after 6 iterations
#     iteration_count += 1
#     if iteration_count > max_iterations:
#         break
#     elif iteration_count == 7:
#         is_server_turn = False  # Switch to client phase

#     # Display the final combined image
#     cv2.imshow('Server - Camera Feeds', background_copy)

#     # End condition and key press handling
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# client_socket.close()
# cap.release()
# cv2.destroyAllWindows()




# import cv2
# import socket
# import pickle
# import struct
# import mediapipe as mp

# # Initialize MediaPipe and socket
# mp_hands = mp.solutions.hands
# mp_draw = mp.solutions.drawing_utils
# hands = mp_hands.Hands()

# # Initialize socket for client-server communication
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 9999))
# server_socket.listen(1)
# print('Waiting for client connection...')
# client_socket, addr = server_socket.accept()
# print('Client connected:', addr)

# # Load the background image
# background_image = cv2.imread('score.jpg')

# # Open the server's camera feed
# cap = cv2.VideoCapture(0)

# # Variables for tracking iteration, points, and phase
# iteration_count = 1
# max_iterations = 12
# server_points = 0
# client_points = 0
# is_server_turn = True  # First 6 for server, next 6 for client

# def detect_fingers(image):
#     """Detect fingers and draw landmarks, returning finger array."""
#     finger_array = [0, 0, 0, 0, 0]
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     result = hands.process(image_rgb)
    
#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             landmarks = hand_landmarks.landmark
#             tolerance = 0.005

#             # Detect each finger state
#             thumb_tip, thumb_ip = landmarks[4], landmarks[3]
#             index_tip, index_dip = landmarks[8], landmarks[7]
#             middle_tip, middle_dip = landmarks[12], landmarks[11]
#             ring_tip, ring_dip = landmarks[16], landmarks[15]
#             pinky_tip, pinky_dip = landmarks[20], landmarks[19]
            
#             finger_array[0] = 1 if thumb_tip.x < thumb_ip.x - tolerance else 0
#             finger_array[1] = 1 if index_tip.y < index_dip.y - tolerance else 0
#             finger_array[2] = 1 if middle_tip.y < middle_dip.y - tolerance else 0
#             finger_array[3] = 1 if ring_tip.y < ring_dip.y - tolerance else 0
#             finger_array[4] = 1 if pinky_tip.y < pinky_dip.y - tolerance else 0

#     return finger_array, image

# # Payload size for receiving client frame data
# data = b""
# payload_size = struct.calcsize("Q")

# while True:
#     # Capture server camera frame
#     success, server_frame = cap.read()
#     if not success:
#         break
    
#     # Resize and set up background
#     server_frame_resized = cv2.resize(cv2.flip(server_frame, 1), (450, 654))
#     background_copy = background_image.copy()
#     background_copy[0:654, 0:450] = server_frame_resized

#     # Receive and process client frame
#     while len(data) < payload_size:
#         packet = client_socket.recv(4096)  # Receive 4K bytes at a time
#         if not packet:
#             break
#         data += packet
#     packed_msg_size = data[:payload_size]
#     data = data[payload_size:]
#     msg_size = struct.unpack("Q", packed_msg_size)[0]

#     # Retrieve the actual frame data from client
#     while len(data) < msg_size:
#         data += client_socket.recv(4096)
#     client_frame_data = data[:msg_size]
#     data = data[msg_size:]

#     # Unpickle the client frame data
#     client_frame = pickle.loads(client_frame_data)
#     client_frame_resized = cv2.resize(cv2.flip(client_frame, 1), (450, 654))
#     background_copy[0:654, 550:1000] = client_frame_resized

#     # Detect fingers for server and client
#     server_fingers, server_frame_with_landmarks = detect_fingers(server_frame_resized)
#     client_fingers, client_frame_with_landmarks = detect_fingers(client_frame_resized)

#     # Display server and client fingers array on screen
#     cv2.putText(background_copy, f"Server Fingers: {server_fingers}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(background_copy, f"Client Fingers: {client_fingers}", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     # Points update logic
#     if is_server_turn:
#         if server_fingers != client_fingers:
#             server_points += sum(server_fingers)
#     else:
#         if server_fingers != client_fingers:
#             client_points += sum(client_fingers)

#     print(f"Server Points: {server_points}, Client Points: {client_points}")

#     # Show current points
#     cv2.putText(background_copy, f"Server Points: {server_points}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(background_copy, f"Client Points: {client_points}", (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     # Display iteration
#     cv2.putText(background_copy, f"Iteration: {iteration_count}", (420, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 6)

#     # Update iteration count and switch turn after 6 iterations if hands are detected correctly
#     if server_fingers != [0, 0, 0, 0, 0] and client_fingers != [0, 0, 0, 0, 0]:
#         iteration_count += 1
#         if iteration_count == 7:
#             is_server_turn = False  # Switch to client phase
#     if iteration_count > max_iterations:
#         break

#     # Display the final combined image
#     cv2.imshow('Server - Camera Feeds', background_copy)

#     # End condition and key press handling
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# client_socket.close()
# cap.release()
# cv2.destroyAllWindows()



import cv2
import socket
import pickle
import struct
import mediapipe as mp
import time

# Initialize MediaPipe and socket
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Initialize socket for client-server communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen(1)
print('Waiting for client connection...')
client_socket, addr = server_socket.accept()
print('Client connected:', addr)

# Load the background image
background_image = cv2.imread('sc.jpg')

# Open the server's camera feed
cap = cv2.VideoCapture(0)

# Variables for tracking iteration, points, and phase
iteration_count = 1
max_iterations = 12
server_points = 0
client_points = 0
is_server_turn = True  # First 6 for server, next 6 for client

server_fingers = [0, 0, 0, 0, 0] 
client_fingers = [0, 0, 0, 0, 0]

# Timer variables
start_timer = False
timer_start_time = None
countdown_seconds = 3  # 3 seconds countdown

cv2.putText(background_image, str("Press 's' to Start"), (70, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.putText(background_image, str("Press 'q' to Quit"), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.putText(background_image, str("Press 'p' to Play Again"), (910, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


def detect_fingers(image):
    """Detect fingers and draw landmarks, returning finger array."""
    finger_array = [0, 0, 0, 0, 0]
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(image_rgb)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            tolerance = 0.005

            # Detect each finger state
            thumb_tip, thumb_ip = landmarks[4], landmarks[3]
            index_tip, index_dip = landmarks[8], landmarks[7]
            middle_tip, middle_dip = landmarks[12], landmarks[11]
            ring_tip, ring_dip = landmarks[16], landmarks[15]
            pinky_tip, pinky_dip = landmarks[20], landmarks[19]
            
            finger_array[0] = 1 if thumb_tip.x < thumb_ip.x - tolerance else 0
            finger_array[1] = 1 if index_tip.y < index_dip.y - tolerance else 0
            finger_array[2] = 1 if middle_tip.y < middle_dip.y - tolerance else 0
            finger_array[3] = 1 if ring_tip.y < ring_dip.y - tolerance else 0
            finger_array[4] = 1 if pinky_tip.y < pinky_dip.y - tolerance else 0

    return finger_array, image

# Payload size for receiving client frame data
data = b""
payload_size = struct.calcsize("Q")

while True:
    # Capture server camera frame
    success, server_frame = cap.read()
    if not success:
        break
    
    # Resize and set up background
    server_frame_resized = cv2.resize(cv2.flip(server_frame, 1), (600, 600))
    background_copy = background_image.copy()
    background_copy[200:800,:600] = server_frame_resized

    # Receive and process client frame
    while len(data) < payload_size:
        packet = client_socket.recv(4096)  # Receive 4K bytes at a time
        if not packet:
            break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    # Retrieve the actual frame data from client
    while len(data) < msg_size:
        data += client_socket.recv(4096)
    client_frame_data = data[:msg_size]
    data = data[msg_size:]

    # Unpickle the client frame data
    client_frame = pickle.loads(client_frame_data)
    client_frame_resized = cv2.resize(cv2.flip(client_frame, 1),(600, 600))
    background_copy[200:800, 800:1400] = client_frame_resized
    


    # Start countdown when 's' is pressed
    if start_timer:
        elapsed_time = time.time() - timer_start_time
        if elapsed_time < countdown_seconds:
            countdown_value = countdown_seconds - int(elapsed_time)
            cv2.putText(background_copy, str(countdown_value), (650, 500), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)
        else:
            cv2.putText(background_copy, "Play", (600, 500), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)

            # Detect fingers for server and client
            server_fingers, server_frame_with_landmarks = detect_fingers(server_frame_resized)
            client_fingers, client_frame_with_landmarks = detect_fingers(client_frame_resized)
            
            
            print(f"Server Fingers: {server_fingers}, Client Fingers: {client_fingers}")
            
            # Display server and client fingers array on screen


            # Points update logic
            if is_server_turn:
                if server_fingers != client_fingers:
                    if server_fingers[0]==1 and sum(server_fingers)==1:
                        server_points+=6
                    else:
                        server_points += sum(server_fingers)                            
                    
            else:
                if server_fingers != client_fingers:
                    if client_fingers[0]==1 and sum(client_fingers)==1:
                        client_points+=6
                    else:
                      client_points += sum(client_fingers)  
                    
            print(f"Server Points: {server_points}, Client Points: {client_points}")
            print(f"Iteration Count{iteration_count}")
            # Display current points and iteration count




            # Increment iteration if both hands are detected properly
            if server_fingers != [0, 0, 0, 0, 0] and client_fingers != [0, 0, 0, 0, 0]:
                iteration_count += 1
                if iteration_count >6:
                    is_server_turn = False  # Switch to client phase
                elif iteration_count > max_iterations:
                    break
            start_timer = False  # Reset timer

    cv2.putText(background_copy, f"Server Fingers: {server_fingers}", (50, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(background_copy, f"Client Fingers: {client_fingers}", (820, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)    # cv2.putText(background_copy, f"Server Points: {server_points}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    # cv2.putText(background_copy, f"Client Points: {client_points}", (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(background_copy, f"Iteration: {iteration_count}", (610, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(background_copy, f"Server Points: {server_points}", (200, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(background_copy, f"Client Points: {client_points}", (920, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


    cv2.imshow('Server - Camera Feeds', background_copy)
    
    # Key handling
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

        
        
    if key & 0xFF == ord('s') and not start_timer and iteration_count <= max_iterations:
        start_timer = True
        timer_start_time = time.time()


    # Display the combined image

if server_points>client_points:
    cv2.putText(background_copy, f"Winner Server{server_points}", (610, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
elif server_points<client_points:
    cv2.putText(background_copy, f"Winner Client{client_points}", (610, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
else:
    cv2.putText(background_copy, str("Match Draw"), (610, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    

cv2.imshow('Server - Camera Feeds', background_copy)

# key = cv2.waitKey()
# if key & 0xFF == ord('p'):


key = cv2.waitKey()
if key & 0xFF == ord('e'):
    client_socket.close()
    cap.release()
    cv2.destroyAllWindows()
