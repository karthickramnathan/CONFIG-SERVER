import socket
import os
import threading
import hashlib


# Create Socket (TCP) Connection
ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1233
ThreadCount = []
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waitiing for a Connection..')
ServerSocket.listen(5)
HashTable = {}

# Function : For each client 
def threaded_client(connection):
    connection.send(str.encode('ENTER USERNAME (max char 5): ')) # Request Username
    for i in range(0,5):
        name = connection.recv(2048)
    connection.send(str.encode('ENTER PASSWORD (max char 5): ')) # Request Password
    for i in range(0,5):
        password = connection.recv(2048)
    password = password.decode()
    name = name.decode()
    password=hashlib.sha256(str.encode(password)).hexdigest() # Password hash using SHA256
# REGISTERATION PHASE   
# If new user,  regiter in Hashtable Dictionary  
    if name not in HashTable:
        HashTable[name]=password
        connection.send(str.encode('Registeration Successful')) 
        print('Registered : ',name)
        print("{:<8} {:<20}".format('USER','PASSWORD'))
        for k, v in HashTable.items():
            label, num = k,v
            print("{:<8} {:<20}".format(label, num))
        print("-------------------------------------------")
        
    else:
# If already existing user, check if the entered password is correct
        if(HashTable[name] == password):
            connection.send(str.encode('Connection Successful')) # Response Code for Connected Client 
            print('Connected : ',name)
            while True:
                data=connection.recv(1024)
        else:
            connection.send(str.encode('Login Failed')) # Response code for login failed
            print('Connection denied : ',name)
           

while True:
    Client, address = ServerSocket.accept()
    client_handler = threading.Thread(
        target=threaded_client,
        args=(Client,)  
    )
    client_handler.daemon=True
    client_handler.start()
    ThreadCount.append(Client)
    print('Connection Request: ' + str(ThreadCount))
ServerSocket.close()
