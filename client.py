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
    print("Try again"+str(e))
    sock.close()
    sys.exit()

print("Type your Message")
try:
    a=raw_input("You: ").encode()
    while True:
        #encoding to byte
        if not a or 'exit' in a or 'logout' in a or 'thank you' in a or 'bye' in a:
            sock.send(a)
            time.sleep(1)
            print("Server: Thank you")
            print("Server Disconnected...")
            sock.close()
            break

        else:
            a=bytes(a)
            sock.send(a)
            #sending the input as input is not from file b' is not used
            b=sock.recv(1024)
            nw=str(b)
            #if the string contains following words server will be disconnected

            if 'exit' in nw or 'logout' in nw or 'thank you' in nw or 'bye' in nw:
                sock.send(b'thank you')
                time.sleep(1)
                print('Server: '+b)
                print('Server Disconnected...')
                sock.close()
                sys.exit()

            else:
                print("Server: "+b)
                a=raw_input("You: ").encode()

except KeyboardInterrupt as k:#making KeyboardInterrupt reasonable
    print("\nDisconnected...")
    sock.send(b'exit')
    time.sleep(1)
    sock.close() #closing the socket
    sys.exit()

sock.close()
