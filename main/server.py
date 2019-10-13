'''
Created on October 9, 2019

@author: Brad Bosak
'''
import socket
import sys

class Server:
    def createServer(self):
        #Create server socket
        serverSocket = socket.socket()          
        
        #Define port and bind
        caPort = 9501
        port = 9500
        
        serverSocket.bind(('', port))
        serverSocket.listen(5)
              
        print ("Server socket is created, binded to port {0}, and listening".format(port))
        
        #server attributes
        serverName="BradsServer"
        
        while True:
            
            #Find client
            (clientSocket, address) = serverSocket.accept()
            print ("Connection found from ", address)
            dataFromClient = clientSocket.recv(1024).decode()
            
            #Logic around messages
            if dataFromClient == "Name":
                returnMessage = serverName
            else:
                returnMessage = "Goodbye"
            #Print client message and send return message
            print ('Message from client is:', dataFromClient)
            clientSocket.send(returnMessage.encode())
    
def main():
    server = Server()
    server.createServer()
 
main()