'''
Created on October 9, 2019

@author: Brad Bosak
'''
import socket
# from Crypto.Cipher import AES

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

    def encrypt(self, phrase, publicKey):
        print("public key is ", publicKey)
        encryptedValue = []
        for i in range(len(phrase)):
            x = ord(phrase[i]) + ord(publicKey[i])
            encryptedValue.append(chr(x))
            encryptedString = ''.join(encryptedValue)
        print("the encrypted string is ", encryptedString)
        return(encryptedString)
            
    def decrypt(self, encryptedValue, publicKey):
        decryptedValue = []
        for i in range(len(encryptedValue)):
            x = ord(encryptedValue[i]) - ord(publicKey[i])
            decryptedValue.append(chr(x))
        print("the decrypted value is ", decryptedValue)
        return(decryptedValue)
    
    def sendCipherPhraseToServer(self, encryptedValue):
        #Create client socket
        clientSocket = socket.socket()
        
        #Define port
        serverPort = 9500
        
        #Connect to server to get server's name
        clientSocket.connect(('127.0.0.1', serverPort))
            
        serverMessage = encryptedValue
        #Send message to server
        clientSocket.send(serverMessage.encode())
        #Receive and print server name
        serverAcknowledge = clientSocket.recv(1024).decode()
        print("Did the server acknowledge? ", serverAcknowledge)
        return(serverAcknowledge)

def main():
    cipherPhrase = "session cipher phrase"
    client = Client()
    serverName = client.clientToServer()
    publicKey = client.clientToCA(serverName)
    encryptedString = client.encrypt(cipherPhrase, publicKey)
    sendCipherPhraseToServer(encryptedString)
    # decryptedValue = client.decrypt(encryptedValue, publicKey)
 
main()