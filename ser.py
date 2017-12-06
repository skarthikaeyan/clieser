import socket
import sys
import string
import time
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host=socket.gethostname()
port=65535
try:
    sock.bind((host,port))
except socket.error as e:
    print("error",e)
    sys.exit()
sock.listen(2)
print("Waiting for connection...")
com, addr = sock.accept()
print("Connected to"+str(addr).strip('()'))

a = com.recv(1024).decode()
a=str(a)
a=a.lower()
a=a.replace("'","")
if a=='exit' or a== 'logout' or a=='bye':
    com.send(b'Terminate')
    sys.exit()
print("received ", a)
words=a.split()
length=len(words)
i=0
while True:
    if not a:
        print("No Input, Thank you")
        break
    else:
        if words[0]=="hello":
            c="Hi "
        else:
            c="Hello "
        if words[i]!="hello" and words[i]!="hi" and words[i]!="im":
            w = words[i]
            w=w.capitalize()
            w = c + w
            #print(a)
            #print (w)
            #print(w)
            w.encode()
            time.sleep(1)
            com.send(w)
            time.sleep(2)
            com.send(b'Terminate')
            com.close()
            sys.exit()
        else:
            i+=1
            continue
