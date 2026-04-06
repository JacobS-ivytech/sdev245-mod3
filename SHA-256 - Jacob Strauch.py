import hashlib

def HashString(msg):
    return hashlib.sha256(msg.encode()).hexdigest()

#function will take a file name and hash the data within
def HashFile(file):
    msgFile = open(file, 'rb')
    msg = msgFile.read()
    msgFile.close()
    return hashlib.sha256(msg.encode()).hexdigest()

message = input("Input message to hash: ")
hashMessage = HashString(message)
print(hashMessage)