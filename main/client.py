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

    # def encrypt(self, phrase, publicKey):
    #     encryption = []
    #     for i in range(len(phrase)):
    #         x = (ord(phrase[i]) +
    #             ord(publicKey[i])) % 26
    #         x += ord('A') 
    #         encryption.append(chr(x))
    #     encryptedValue = "" . join(encryption)
    #     print("the encrypted value is ", encryptedValue)
    #     return(encryptedValue)
    
    # def decrypt(self, encryption, publicKey): 
    #     originalPhrase = [] 
    #     for i in range(len(encryption)): 
    #         x = (ord(encryption[i]) - 
    #             ord(publicKey[i]) + 26) % 26
    #         x += ord('A') 
    #         originalPhrase.append(chr(x))
    #     decryptedValue = "" . join(originalPhrase)
    #     print("the decrypted value is ", decryptedValue)
    #     return(decryptedValue)

    def encrypt(self, phrase, publicKey):
        encryptedValue = []
        for letter in phrase:
            encryptedValue.append(ord(letter))
        print("the encrypted value is ", encryptedValue)
            
    def decrypt(self, encryption, publicKey):
        decryptedValue = []
        for letter in encryption:
            decryptedValue.append(chr(letter))
        print("the decrypted value is ", decryptedValue)

                
def main():
    client = Client()
    serverName = client.clientToServer()
    publicKey = client.clientToCA(serverName)
    encryptedValue = client.encrypt("session cipher phrase", publicKey)
    decryptedValue = client.decrypt(encryptedValue, publicKey)
 
main()