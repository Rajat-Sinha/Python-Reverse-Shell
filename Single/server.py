import socket # socket is a way to connect between two computers and have conversation
import sys # it is used to run system commands

#create socket (allows two computer to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port  = 9999
        s = socket.socket() #this is the actual socket or conversation between computers
    except socket.error as msg:
        print('Socket Creation Error: '+ str(msg))

#Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print('Binding socket to port: '+str(port))
        s.bind((host, port))# function for bindning socket to port
        s.listen(5)#Listen function allows your server to accept connection


    except socket.error as msg:
        print('Socket Binding Error: '+ str(msg)+"\n" + 'Retrying....')
        socket_bind()

#Establish a connection with Client(socket must be listening for them)

def socket_accept():
    conn,address = s.accept()#conn is a refernce to the connection itself
    print('Connection Established | Ip: ' + str(address[0]) + ' | Port: '+str(address[1]))
    send_commands(conn)
    conn.close()

#Send Command
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024) , 'utf-8') #conn.recv(1024) this is theresponse we get in bytes,1024 is the  buffersize
            print(client_response, end='')

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()