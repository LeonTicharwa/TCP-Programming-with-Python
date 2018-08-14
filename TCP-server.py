import socket
import sys
import time
x = 0
host =  '192.168.1.9'
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("socket created")

try:
     s.bind((host,port))
except:
    print ("binding failed")
    sys.exit()

print ("socket has been bounded")
s.listen(10)
print("socket is ready")

conn, addr = s.accept()

print ("conected with" + addr[0] + ":" + str(addr[1]))
while 1:
 x +=1
 data = conn.recv(4096)
 print("recieved:" + str(x)  + data.decode())
 conn.sendall(data)
 time.sleep(0.005)
print(data.decode)
conn.close()
s.close()

