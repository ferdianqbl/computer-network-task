import sys
import socket
import logging
import json
import time

#set basic logging
logging.basicConfig(level=logging.INFO)

def get_json_data_file():
    file = open("person1.json", "r")
    res = json.load(file)
    # mengembalikan result sebagai string
    return json.dumps(res)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('36b9b80dbf7a', 10000)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data
    # message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    message = get_json_data_file()
    logging.info(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        logging.info(f"{data}")
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    time.sleep(20)
    sock.close()
