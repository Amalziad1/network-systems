from datetime import date
from socket import * 

serverPort = 6000
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))
# Listen to at most 1 connection at a time
serverSocket.listen(1)
print("The server is ready to receive")
# Server should be up and running and listening to the incoming connections
flage=1#check if page end with html is it main page
while True:
 # Set up a new connection from the client
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024).decode()
     print(addr)# print the address
     print(sentence)
     ip = addr[0]
     port = addr[1]
     request = sentence.split()[1]
     m=sentence.split()[1]
     m2=m.split('.')[0]
     myF=m2.split('/')[1]# get the file name
     print("***")
     print("The Request")
     print(request)
     print("***")
 # to get index without HTTP
     if request== "/index.html" or request== "/":# if the request was index.html or empty it will return the main.html file
         flage = 0# if the request done make the flage false
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send("Content-Type: text/html \r\n".encode())
         connectionSocket.send("\r\n".encode())
         filex = open("main.html", "rb")
         connectionSocket.send(filex.read())
         connectionSocket.close()
     elif request.endswith('.html') :# if the request was end with .html return html file
         if (flage==0):# if we entered the previous request continue from the next if statment
             continue
         elif(flage==1):
             connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
             connectionSocket.send("Content-Type: text/html\r\n".encode())
             connectionSocket.send("\r\n".encode())
             filex = open(myF+".html", "rb")
             connectionSocket.send(filex.read())
             connectionSocket.close()
     elif request.endswith('.png'):
 # Send one HTTP header line into socket
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send("Content-Type: image/png \r\n".encode())
         connectionSocket.send("\r\n".encode())
         s = open(myF+".png", "rb")
 # Close the client connection socket
         connectionSocket.send(s.read())
         connectionSocket.close()
     elif request.endswith('.jpg'):
 # Send one HTTP header line into socket
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send("Content-Type: image/jpeg\r\n".encode())
         connectionSocket.send("\r\n".encode())
         s = open(myF+".jpeg", "rb")
 # Close the client connection socket
         connectionSocket.send(s.read())
         connectionSocket.close()
     elif request.endswith('.css'):
 # Send one HTTP header line into socket
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send("Content-Type: text/css \r\n".encode())
         connectionSocket.send("\r\n".encode())
         s = open(myF + ".css", "rb")
 # Close the client connection socket
         connectionSocket.send(s.read())
         connectionSocket.close()
     elif request.endswith('SortByName'):
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send("Content-Type: text/html \r\n".encode())
         connectionSocket.send("\r\n".encode())
         my_file = open("SortedByName.html", "r")# read the file with sorted data
         connectionSocket.send(html.encode())
         connectionSocket.close()
     elif request.endswith('SortByPrice'):
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send("Content-Type: text/html \r\n".encode())
         connectionSocket.send("\r\n".encode())
         my_file = open("SortByPrice", "r")
         connectionSocket.send(html.encode())
         connectionSocket.close()
     else:# if the request didn't end with any of the previous option display an error
         connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
         connectionSocket.send("Content-Type: text/html")
         connectionSocket.send("\r\n".encode())
         my_file = open("error.html", "r")
         connectionSocket.send(s.encode())
         connectionSocket.close()
