import random
import time

crypting_value = random.randint(0, 9999)
starting_value = crypting_value
step = 0


codeables = [" ",".",",","0","1","2","3","4","5","6","7","8","9","$","'",'"',"+","#","!","?","€", "a", "A", "b", "B","c", "C","d", "D","e", "E","f", "F","g", "G","h", "H","i", "I","j", "J","k", "K","l", "L","m", "M","n", "N","o", "O","p", "P","q", "Q","r", "R","s", "S","t", "T","u", "U","v", "V","w", "W","x", "X","y", "Y","z", "Z"]

print("[1] encrypt")
print("[2] decrypt")

command = int(input())

deletion = "not an int"

if command == 1:
    print("enter message to encrypt (only upper and lowercase letters, spaces, commas (,) and dots (.)).")
    to_encrypt = list(input())
    print(to_encrypt)
    message_len = len(to_encrypt)
    skip = crypting_value
    encrypted = []
    while step != message_len:
        print(step)
        print(len(to_encrypt))
        encrypting = to_encrypt[step]
        pos = codeables.index(str(encrypting))
        if skip >= len(codeables):
            skip = skip%len(codeables)
        finalskip = pos + skip
        if finalskip >= len(codeables):
            finalskip = finalskip%len(codeables)
        encrypted.append(codeables[finalskip]) 
        step = step + 1
        skip = skip + 1
    result = open("result.txt", "w")
    result.write("".join(encrypted))
    print("encryption complete.\n\n")
    print(f"The decryption key is {crypting_value}")
    time.sleep(20)
elif command == 2:
    print("insert message to decrypt.")
    to_decrypt = list(input())
    print(to_decrypt)
    message_len = len(to_decrypt)
    importantvalue = int(input("input starting value from the encryption process... "))
    decrypted = []
    sidestep = 0
    skip = importantvalue
    while step != message_len:

        decrypting = to_decrypt[step]
        pos = codeables.index(str(decrypting))
        if skip >= len(codeables):
            skip = skip%len(codeables)
        finalskip = pos - skip
        decrypted.append(codeables[finalskip])
        step = step + 1
        skip = skip + 1
    result = open("result.txt", "w")
    result.write("".join(decrypted))
    print("decryption complete.")
    time.sleep(15)
else:
    pass