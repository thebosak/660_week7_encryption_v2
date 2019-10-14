# 660_week7_encryption_v2
660_week7_encryption_v2

Files:
certificateAuthority.py - contains the server name and public key.  Runs on port 9501
server.py - contains instructions on how to receive messages from client.  Runs on port 9500
client.py - gets the name of the server, gets the public key from the CA, encrypts phrase and sends to server, verifies acknowledgment

Description:
Run each of the above files in order.  When the prompt for the client appears, type "Name" which should tell the server you want its name.  The program should take care of the rest.