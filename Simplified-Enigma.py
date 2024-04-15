import random
import time

crypting_value = random.randint(0, 9999)
step = 0

codeables = ["§","/","[","]","@","{","}","<",">","&","*","","|",";","~","`","÷","×","ß","¤","-","_",":", " ",".",",","(",")", "0","1","2","3","4","5","6","7","8","9","$","'",'"',"+","#","!","?","€", "a","á","ä", "A","Á", "b", "B","c","ć","č", "C","Ć","Č","d","ď", "D","Ď","e","é","ě", "E","É","Ě","f", "F","g", "G","h", "H","i","í", "I","Í","j", "J","k", "K","l","ĺ","ľ", "L","Ĺ","Ľ","m", "M","n","ň", "N","Ň","o","ó","ô", "O","Ó","p", "P","q", "Q","r","ŕ","ř", "R","Ŕ","Ř","s","ś","š", "S","Ś","Š","t","ť", "T","Ť","u","ú", "U","Ú","v", "V","w", "W","x", "X","y","ý", "Y","Ý","z","ź","ž", "Z","Ź","Ž"]

print("[1] encrypt")
print("[2] decrypt")
command = int(input())

if command == 1:
    print("Enter message to encrypt.")
    to_encrypt = list(input())
    message_len = len(to_encrypt)
    skip = crypting_value
    encrypted = []
    while step != message_len:
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
    time.sleep(10)
elif command == 2:
    print("insert message to decrypt.")
    to_decrypt = list(input())
    message_len = len(to_decrypt)
    importantvalue = int(input("input starting value from the encryption process... "))
    decrypted = []
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
    time.sleep(10)
else:
    pass
