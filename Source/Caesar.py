import string
from DetectEnglish import *

alphabet = list(string.ascii_lowercase)

def CaesarEncode(text,key):
    ciphertext = ""
    for letter in text:
        if letter in alphabet:
            ciphertext += alphabet[(alphabet.index(letter) + key) % len(alphabet)]
        else:
            ciphertext += letter
    return ciphertext

def CaesarDecode(ciphertext,key,to_upper=False):
    plaintext = ""
    for letter in ciphertext:
        if letter not in alphabet:
            plaintext += letter
        else:
            plaintext += alphabet[(alphabet.index(letter) - key) % len(alphabet)]
    if to_upper == True:
        plaintext = plaintext.upper()
    return plaintext

def CaesarBruteforce(ciphertext):
    plaintexts = []
    for i in range(25):
        possible_plaintext = CaesarDecode(ciphertext,i)
        if len(ciphertext) > 150 and checkEnglish(possible_plaintext):
            return possible_plaintext
        else:
            plaintexts.append(possible_plaintext)
    return "\n\n".join(plaintexts)
