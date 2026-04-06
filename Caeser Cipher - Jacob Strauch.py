#caeser cipher app
def CaeserEncrypt(msg, shift):
    msg = msg.lower()
    encTxt = ""
    for char in msg:
        if char.islower():
            encTxt += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encTxt += char
    return encTxt

#take input message
ogMessage = input("Enter text to be encoded: ")

#encrypt message
encMessage = CaeserEncrypt(ogMessage, 15)

#display encrypted message
print("Encoded Message: " + encMessage)

#decrtpt message
decMessage = CaeserEncrypt(encMessage, -15)

#display decrypt message
print("Decoded Message: " + decMessage)