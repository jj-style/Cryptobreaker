import string
from RemovePunctuation import *

alphabet = list(string.ascii_lowercase)

def BeaufortEncode(text,key,german=False):
    ciphertext = ""
    text_count = 0
    key_count = 0
    while text_count < len(text):
        if text[text_count] in alphabet:
            if not german:
                ciphertext += alphabet[(alphabet.index(key[key_count%len(key)]) - alphabet.index(text[text_count])) % len(alphabet)]
            elif german:
                ciphertext += alphabet[(alphabet.index(text[text_count]) - alphabet.index(key[key_count%len(key)])) % len(alphabet)]
            text_count += 1
            key_count += 1
        else:
            ciphertext += text[text_count]
            text_count += 1
    return ciphertext

def BeaufortDecode(text,key,german=False):
    plaintext = ""
    text_count = 0
    key_count = 0
    while text_count < len(text):
        if text[text_count] in alphabet:
            if not german:
                plaintext += alphabet[(alphabet.index(key[key_count%len(key)]) - alphabet.index(text[text_count])) % len(alphabet)]
            elif german:
                plaintext += alphabet[(alphabet.index(text[text_count]) + alphabet.index(key[key_count%len(key)])) % len(alphabet)]
            text_count += 1
            key_count += 1
        else:
            plaintext += text[text_count]
            text_count += 1
    return plaintext
