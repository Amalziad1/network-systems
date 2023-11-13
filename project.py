import socket
import os
def viewpage(path):
    if (path == '/main.html'): 
            header = 'HTTP/1.1 200 OK\n' + 'Content-Type: text/html \n\n'
            response="<!DOCTYPE html><html><head><link rel='stylesheet' href='css.css'><title>ENCS3320-Simple Webserver</title><meta name='viewport' content='width=device-width, initial-scale=1'><link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'><body><div class='w3-container w3-teal'><h1>Welcome to <span style='color:white'> Computer Networks</h1></div><style type=text/css>.up{float: left;}.middlediv{float: left;}.down{float: left;}div{padding : 1%;font-style: Arial;background-color:#B7D5C7;width: 100%;border: solid black;}</style></head><body><div class='up'><h1>Amal Ziad</h1><p><center>Amal is a 3rd year student, majoring computer</p><p>engineering at Birzeit University.The ID number</p><p>is 1192141. She has skills in graphic design and</p><p>art. Projects that she had done are security, python,</p><p>java, in different courses.</p><h2><right><img src='amal.jpg' alt='amal' style='width:30%'></h2></div><div class='middlediv'><h1>Sereen AbuZayed</h1><p><center>Sereen is a 3rd student, majoring computer science</p><p>and minor business administration at Birzeit </p><p>University. The ID number is 1193073. She has skills</p><p>in c programming and volunteering in diiferent ways.</p><p>Projects that she had done are data strucure, data </p><p>base, c programming, in different courses.</p><h2></h2><img src='sereen.jpg' alt='sereen' style='width:30%'></div><div class='rightdiv'><h1>Malak Taha</h1><p><center>Malak is a 3rd student, majoring computer science</p><p>at Birzeit University. The ID number is 1190679. </p><p>She has skills in java programming and in algorithms. </p><p>Projects that she had done are data strucure, data </p><p>base, java programming, in different courses.</p><h2></h2><img src='malak.jpg' alt='malak' style='width:30%'></div><div><p>Port Number:6000</p><p>IP Address:192.168.176.73</p></body></html>"

    elif (path == '/2'):
        file = open('view1.html', 'rb')
        response = file.read()
        file.close()
        header = 'HTTP/1.1 200 OK\n' + 'Content-Type: text/html \n\n'
    elif (path == '/3'):
        file = open('img.jpg', 'rb')
        response = file.read()
        file.close()
        header = 'HTTP/1.1 200 OK\n' + 'Content-Type: image/jpg \n\n'
    else:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response ="<html><head><title>Error</title><body><p><span style='color:red'>The file is not found</p><p><b>Amal-1192141</p><p>Sereen-1193073</p><p>Malak-1190679</b></p><p>IP Address:192.168.176.73</p><p>Port Number:6500</p></body></html>"
        connection.send(header.encode() + response)
        connection.close()
def get_path(request):
    try:
        l= request.split(' ')
        return l[1]
    except :
        return "error"
HOST= '172.19.44.217'
PORT= 6500
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((HOST, PORT))
ServerSocket.listen(1)
print('webserver serving on port: ', PORT)
while True:
    connection, address = ServerSocket.accept()
    ip, port = ServerSocket.getsockname()
#decode as 8 bit characters
    request = connection.recv(1024).decode()
    print("------------------------------------------------------------------")
    print(request)
    print("------------------------------------------------------------------")
    #get the path
    path = get_path(request)
    viewpage(path)
