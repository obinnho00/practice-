import socket
class server:
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 2468))
    s.listen(5)

    """ waite when you get a request"""
    while True:
        #s.send("welcome to AIO cheat system!")
        incoming_message, address = s.accept()
        print( "connection from", address,"has been exterblished!")
        incoming_message.send(bytes("welcome to aio cheat system!", "utf-8"))
        incoming_message.close()
        
        
server()



