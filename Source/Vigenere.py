import string
from RemovePunctuation import *

alphabet = list(string.ascii_lowercase)

def VigenereEncode(text,key):
    ciphertext = ""
    text_count = 0
    key_count = 0
    while text_count < len(text):
        if text[text_count] in alphabet:
            ciphertext += alphabet[(alphabet.index(text[text_count]) + alphabet.index(key[key_count%len(key)])) % len(alphabet)]
            key_count += 1
            text_count += 1
        else:
            ciphertext += text[text_count]
            text_count += 1
    return ciphertext

def VigenereDecode(text,key):
    plaintext = ""
    text_count = 0
    key_count = 0
    while text_count < len(text):
        if text[text_count] in alphabet:
            plaintext += alphabet[(alphabet.index(text[text_count]) - alphabet.index(key[key_count%len(key)])) % len(alphabet)]
            key_count +=1
            text_count+=1
        else:
            plaintext += text[text_count]
            text_count += 1
    return plaintext


