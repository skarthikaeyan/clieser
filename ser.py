import socket
import sys
import string
import time

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create a socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#reuse the socket once more if not closed properly
host=socket.gethostname()
port=65535


try:
    sock.bind((host,port))
except socket.error as e:
    print("error",e)
    sys.exit()

sock.listen(1)
print("Waiting for connection...")
com, addr = sock.accept()
print("Connected to " + str(addr).strip('()'))

try:
    a = com.recv(1024).decode()
    a=str(a)
    a=a.lower()
    a=a.replace("'","") #making the string readble for program

    if 'exit' in a or 'logout' in a or 'thank you' in a or 'bye' in a or not a:
        print("Client: "+a)
        com.close()
        time.sleep(1)
        print("Client disconnected...")
        sys.exit()

    print("Client: "+a)
    words=a.split()
    length=len(words)
    i=0

    while True:#frist while loop is for processing the introduction runs only once
        if not a:
            print("No Input")
            com.send(b'thank You')
            time.sleep(1)
            com.close()
            sys.exit()

        else:

            if words[0]=="hello":
                c="Hi "

            else:
                c="Hello "

            if words[i]!="hello" and words[i]!="hi" and words[i]!="im":
                w = words[i]
                w=w.capitalize()
                w = c + w
                w.encode()
                com.send(w)
                print('You: '+w)
                time.sleep(1)
                break

            else:
                i+=1
                continue
#infinite loops error occurs when i put following code above
    while True:#second while is for 1 to 1 communication
        nw=com.recv(1024)
        nw=str(nw)
        nw=nw.lower()

        if 'exit' in nw or 'logout' in nw or 'thank you' in nw or 'bye' in nw or not nw:
            print("Client: "+nw)
            com.send(b'thank you')
            print("Client Disconnected...")#to check client sends exit message
            time.sleep(1)
            com.close()
            sys.exit()

        else:
            print("Client: "+nw)
            sdata=raw_input("You: ")

            if 'exit' in sdata or 'logout' in sdata or 'thank you' in sdata or 'bye' in sdata  or not sdata:
                com.send(sdata)
                com.close()
                time.sleep(1)
                sys.exit() #to check server sends exit message

            sdata=sdata.decode()
            com.send(sdata)

except KeyboardInterrupt as k:
    com.send(b'thank you')#KeyboardInterrupt to make readable
    print("Disconnected...")
    time.sleep(1)
    com.close()
    sys.exit()

com.close()
