import string
from RemovePunctuation import *

alphabet = list(string.ascii_lowercase)

def VigenereEncode(text,key):
    text = RemovePunctuation(text)
    ciphertext = ""
    for i in range(len(text)):
        ciphertext += alphabet[(alphabet.index(text[i]) + alphabet.index(key[i%len(key)])) % len(alphabet)]
    return ciphertext

def VigenereDecode(text,key):
    text = RemovePunctuation(text)
    plaintext = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            plaintext += alphabet[(alphabet.index(text[i]) - alphabet.index(key[i%len(key)])) % len(alphabet)]
        else:
            plaintext += text[i]
    return plaintext
