import rsa

#message to encrypt
ogMessage = input("Enter message to be hashed: ")

#convert to bytes
messageBytes = ogMessage.encode()

#generate asymmetric key pair
publicKey, privateKey = rsa.newkeys(2048)

#find SHA-256 hash value
hashValue = rsa.compute_hash(messageBytes, 'SHA-256')

#sign message with private key
signature = rsa.sign(messageBytes, privateKey, 'SHA-256')

#verify message is original
rsa.verify(messageBytes, signature, publicKey)