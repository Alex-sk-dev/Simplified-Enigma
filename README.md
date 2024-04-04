# Idea for the project

As the name implies, this python program was inspired by the Nazi germany's encryption device "Enigma".
The code encrypts messages the same way an enigma would with the exception of there being only one
signal turning wheel insstead of 2 or more as were on the original Enigma machines.


# How it works

When you open the program, you will be prompted with 2 options - to encrypt or to decrypt.

Let's start with encryption.
  Upon choosing to encrypt, you will be prompted to write a message to encrypt. Press enter once you are done writing it.
  This will initiate the encryption process of the message which will result in a sort of hash. You will also be given the
  decryption key, which will be needed for the decryption.
  You will have 20 seconds to extract the decryption key.

Option 2 - decryption.
  Upon choosing to decrypt, you will be prompted to enter the message hash from the encryption process to decrypt.
  Upon entering this, you will be prompted to enter the decryption code which you have received from the encryption process.
  Entering the wrong encryption code will result in the decryption failing.
  Upon entering the decryption key, correct or not, the decryption process will run.
  If the decryption key you have entered is correct, you will receive back the message you encrypted.
  If the decryption key you entered is wrong, you will receive a broken up hash.    

In both cases, you will find the resuslt of the operation in a text file named "result.txt" in the same folder as the Enigma progam itself.

# List of supported characters

As the real enigma did, this virtual enigma machine uses a list of characters for the encryption.
If you attempt to use a character which is not in the list, it will break the code. Please, refrain
from using unsupported characters for this very reason.
as for the list itself, here it is:
[" ",".",",","0","1","2","3","4","5","6","7","8","9","$","'",'"',"+","#","!","?","€", "a", "A", "b", "B","c", "C","d", "D","e", "E","f", "F","g", "G","h", "H","i", "I","j", "J","k", "K","l", "L","m", "M","n", "N","o", "O","p", "P","q", "Q","r", "R","s", "S","t", "T","u", "U","v", "V","w", "W","x", "X","y", "Y","z", "Z"]