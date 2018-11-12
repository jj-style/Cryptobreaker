import string
from RemovePunctuation import *

alphabet = list(string.ascii_lowercase)

def BeaufortEncode(text,key,german=False):
    text = RemovePunctuation(text)
    ciphertext = ""
    for i in range(len(text)):
        if not german:
            ciphertext += alphabet[(alphabet.index(key[i%len(key)]) - alphabet.index(text[i])) % len(alphabet)]
        elif german:
            ciphertext += alphabet[(alphabet.index(text[i]) - alphabet.index(key[i%len(key)])) % len(alphabet)]
    return ciphertext

def BeaufortDecode(text,key,german=False):
    text = RemovePunctuation(text)
    plaintext = ""
    for i in range(len(text)):
        if not german:
            plaintext += alphabet[(alphabet.index(key[i%len(key)]) - alphabet.index(text[i])) % len(alphabet)]
        elif german:
            plaintext += alphabet[(alphabet.index(text[i]) + alphabet.index(key[i%len(key)])) % len(alphabet)]
    return plaintext
