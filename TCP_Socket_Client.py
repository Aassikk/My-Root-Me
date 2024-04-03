import socket
import math
import re # regex library
import struct # alows conversion of floats into bytes


def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "challenge01.root-me.org"  # replace with the server's IP address
    server_port = 52002  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))

    while True:
        # input message and send it to the server
        """    
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8")[:1024])
        """

        # receive message from the server
        response = client.recv(1024)
        response = response.decode("utf-8")
        print(response)

        # extract numbers from the message
        numbers = [int(num) for num in re.findall(r'\d+', response)]
        print("Numbers:", numbers)
        if len(numbers) != 2:
            print("Unexpected response from server.")
            return

        # calculate result
        res = math.sqrt(numbers[1]) * numbers[2]
        
        # send answer to server
        client.send( (str(res) + "\n").encode()) 

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
        if response.lower() == "closed":
            break

        print(f"Received: {response}")

    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")
    
run_client()
