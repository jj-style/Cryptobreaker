from Vigenere import *
from RemovePunctuation import *
import string

alphabet = string.ascii_lowercase

def AutokeyEncode(plaintext,key):
    key = key + plaintext
    return VigenereEncode(plaintext,key)

def AutokeyDecode(ciphertext,key):
    key = list(key)
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            current_key = key.pop(0)
            plaintext_letter = VigenereDecode(ciphertext[i],current_key)
            key.append(plaintext_letter)
        else:
            plaintext_letter = ciphertext[i]
        plaintext += plaintext_letter
    return plaintext
