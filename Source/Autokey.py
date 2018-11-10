from Vigenere import *
from RemovePunctuation import *

def AutokeyEncode(plaintext,key):
    key = key + plaintext
    return VigenereEncode(plaintext,key)

def AutokeyDecode(ciphertext,key):
    key = list(key)
    ciphertext = RemovePunctuation(ciphertext)
    plaintext = ""
    for i in range(len(ciphertext)):
        current_key = key.pop(0)
        plaintext_letter = VigenereDecode(ciphertext[i],current_key)
        key.append(plaintext_letter)
        plaintext += plaintext_letter
    return plaintext
