import socket 
from threading import thread 
nickname=input("Choose your name")
server=socket.socket()
ip_address="127.0.0.1"
port=8000
server.connect((ip_address,port))
print("Connected with the server")
def recieve():
    while true:
        try:
        message=server.recv(2048).decode("utf-8")
        if meesage=="NICKNAME":
            server.send(nickname.encode("utf-8"))
        else:
            print(message)
        except:
            print("An error occured")
            server.closed()
            break
        
        
def write():
    while true:
        message=""
        server.send(message.encode("utf-8"))
recieve_thread=thread(target=recieve)
recieve_thread.start()
write_thread=thread(target=write)
write_thread.start()