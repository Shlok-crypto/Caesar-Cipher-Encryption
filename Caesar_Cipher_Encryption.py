# Get text from user
import time

# Encryption Function
def encrypt(text,level):
    text = text
    leterlist = []
    encryptlist = []
    string = ""

# Extracting all the letters from text
    for i in text:
        temp = ord(i)
        leterlist.append(temp)

# Encrypting the letters
    for i in range(len(leterlist)):
        temp2 = leterlist[i]+level
        encryptlist.append(chr(temp2))
        string += chr(temp2)

# Return Statement
    return string, encryptlist


# Decryption Function
def decrypt(encryptlist,level):
    decryptString = ''

# Decrypting the string
    for i in range(len(encryptlist)):
        temp2 = ord(encryptlist[i])
        temp2 = temp2-level
        decryptString += chr(temp2)

    print(f'Decryption Key ==> Caesar Cipher {level}')
    print(f'Decrypted String: {decryptString}')



# Text to Encrypt
text = input("enter text to Encrypt: ")
encryptLeve = int(input("Encryption level: "))

# Encrypting String
string,encryptionlist = encrypt(text,encryptLeve)

print("\nEncryption in process.....\n")
time.sleep(3)
print(string)
print("\nProcess Completed :)")


# Decrypting String
if input("\nWish to decrypt the string? yes or no: ") == "yes":
    print("\nDecryption in process.....\n")
    time.sleep(3)
    decrypt(encryptionlist,encryptLeve)
    print("\nProcess Completed :)")

else:
    print("Process Completed....")
