'''
Created on October 9, 2019

@author: Brad Bosak
'''
import socket
from Crypto.Cipher import AES

class Client:
    def clientToServer(self):
        #Create client socket
        clientSocket = socket.socket()
        
        #Define port
        serverPort = 9500
        
        #Connect to server to get server's name
        clientSocket.connect(('127.0.0.1', serverPort))
            
        serverMessage = input('Enter what you want from the server here: ')
        #Send message to server
        clientSocket.send(serverMessage.encode())
        #Receive and print server name
        serverName = clientSocket.recv(1024).decode()
        print("The server name is ", serverName)
        return serverName
    
    def clientToCA(self, serverName):
        #Create client socket
        clientSocket = socket.socket()
        
        #Define port
        caPort = 9501
        #Connect to CA
        clientSocket.connect(('127.0.0.1', caPort))
        caMessage = serverName
        #Send message to CA
        clientSocket.send(caMessage.encode())
        #Receive and print public key from CA
        dataFromCertificateAuthority = clientSocket.recv(1024).decode()
        print ("Message from CertificateAuthority is", dataFromCertificateAuthority)
        return dataFromCertificateAuthority

    def encrypt(publicKey):
        obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
        message = "The answer is no"
        ciphertext = obj.encrypt(message)
        obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
        print(obj2.decrypt(ciphertext))
                
def main():
    client = Client()
    serverName = client.clientToServer()
    publicKey = client.clientToCA(serverName)
    client.encrypt(publicKey)
 
main()