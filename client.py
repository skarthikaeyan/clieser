import sys
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creating socket sock
host = socket.gethostname() #getting local ip
print(host)
port = 65535
try:
    sock.connect((host,port))
    print("connected")
except socket.error as e:
    print("Try again"+e)
    sys.exit()
print("Type your Message")

a=raw_input("You: ").encode()
while True:
    #encoding to byte
    if not a:
        break
    else:
        a=bytes(a)
        sock.send(a) #sending the input as input is not from file b' is not used
        b=sock.recv(1024)
        if str(b)=='Terminate':
            print('Exiting')
            time.sleep(1)
            print("Server: Thank you")
            break
        else:
            print("Server: "+b)
sock.close() #closing the socket
print("disconnected")
sys.exit()
