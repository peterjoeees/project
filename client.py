import socket 
from threading import thread 
nickname=input("Choose your name")
client=socket.socket()
ip_address="127.0.0.1"
port=8000
client.connect((ip_address,port))
print("Connected with the server")
def recieve():
    while true:
        try:
        message=client.recv(2048).decode("utf-8")
        if meesage=="NICKNAME":
            client.send(nickname.encode("utf-8"))
        else:
            print(message)
        except:
            print("An error occured")
            client.closed()
            break
        
        
def write():
    while true:
        message=""
        client.send(message.encode("utf-8"))
recieve_thread=thread(target=recieve)
recieve_thread.start()
write_thread=thread(target=write)
write_thread.start()