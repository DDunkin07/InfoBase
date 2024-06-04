# echo-server.py

# This program is based on the easy socket example from 
# https://realpython.com/python-sockets/

# This program listens for exactly 1 connection, reads
# an incoming line and sends it right back. It only
# stops if the client disconnects and then terminates.

import socket # load the library

# listen on interface 0.0.0.0. This means the program wants to
# accept connections from any computer on any network. The 
# operating system will forward any data received for the program
# regardly from whom it came
HOST = "0.0.0.0"  

# Port this application is identified by. Any layer 4 segment
# containing this destination port will be forwarded to this application
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # tell the operating system we want to listen to the following 
    # network on the following port
    s.bind((HOST, PORT))
    # start listening for new connections
    s.listen()
    print(f"Listening for new connections on port {PORT}")
    
    # At this point, any data received by the operating system
    # via the network that is:
    # a.) addressed to this computer (Destination IP = this computer's IP)
    # b.) also contains the destination port this application is listening to
    # will be forwarded to this application.

    conn, addr = s.accept() # wait for the next connection to arrive

    with conn:
        print(f"New connection from {addr}")
        while True:
            # data is the content of the layer 4 data unit. So this is
            # already stripped from the headers of layer 1-4, and only
            # contains the information for layers 5-7

            data = conn.recv(1024) # recieve up to 1024 bytes of data
            if not data:
                break # if there was a segment that had an empty data part, quit

            print(f"Received: {data}, replying")
            
            conn.sendall(data) # send all received data right back (echo)
            