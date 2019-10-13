'''
Created on October 9, 2019

@author: Brad Bosak
'''

import socket

class CertificateAuthority:
    def createCaServer(self):
        #Create server socket
        caSocket = socket.socket()          
        
        #Define port and bind
        port = 9501
        caSocket.bind(('', port))
        
        caSocket.listen(5)      
        print ("CA socket is created, binded to port {0}, and listening".format(port))
        
        serverName = "BradsServer"
        publicKey = "Brad is cool"
        
        while True:
            
            #Find client
            (clientSocket, address) = caSocket.accept()
            print ("Connection found from ", address)
            dataFromClient = clientSocket.recv(1024).decode()
            
            #Logic around messages
            if dataFromClient == serverName:
                returnMessage = publicKey
            else:
                returnMessage = "Goodbye"
            #Print client message and send return message
            print ('Message from client is:', dataFromClient)
            clientSocket.send(returnMessage.encode())
            
def main():
    certificateAuthority = CertificateAuthority()
    certificateAuthority.createCaServer()
 
main()