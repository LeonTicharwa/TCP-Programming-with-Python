import serial , string


import time
import socket

hostname, sld, tld, port = '192.168.1.9', 'integralist', 'co.uk', 8000
target = '{}.{}.{}'.format(hostname, sld, tld)

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((hostname, port))


output =  " "

ser = serial.Serial("/dev/USBCurie"  , 300, 8, "N",1,timeout = 50)


while True:
      print "----"
      while output !=  "":
          output = ser.readline()
          print output
          client.send(output)
          time.sleep(0.005)
