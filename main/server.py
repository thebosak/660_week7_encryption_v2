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
        
        #Variables
        publicKey = "Brad is really cool!!"
        cipherPhrase = "session cipher phrase"

        #Define ports
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
            print ('Message from client is: ', dataFromClient)
            clientSocket.send(returnMessage.encode())

            if dataFromClient != "Name":
                serverEncryptedString = getEncryptedCipherPhrase(cipherPhrase, publicKey)
                if serverEncryptedString == dataFromClient:
                    returnMessage = "acknowledged"
            else:
                returnMessage = "I didn't understand the cipher phrase"
            print('Message from client is: ', dataFromClient)
            clientSocket.send(returnMessage.encode())
        
    def getEncryptedCipherPhrase(self, phrase, publicKey):
        print("public key is ", publicKey)
        encryptedValue = []
        for i in range(len(phrase)):
            x = ord(phrase[i]) + ord(publicKey[i])
            encryptedValue.append(chr(x))
            encryptedString = ''.join(encryptedValue)
        print("the encrypted value is ", encryptedString)
        return(encryptedString)
    
def main():
    server = Server()
    server.createServer()
 
main()