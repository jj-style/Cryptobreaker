import string
from Caesar import *

def CreateAlphabet(key,default_alph_shift=0):
    default_alphabet = list(string.ascii_lowercase)
    default_alphabet = list(CaesarEncode("".join(default_alphabet),default_alph_shift))
    new_key = ""
    letters_encountered = []
    for letter in key:
        if letter not in letters_encountered:
            new_key += letter
            letters_encountered.append(letter)
    for letter in new_key:
        default_alphabet.remove(letter)
    alphabet = new_key + "".join(default_alphabet)
    return list(alphabet)

def KeywordSubstitutionEncode(plaintext,key,default_alph_shift=0):
    default_alphabet = list(string.ascii_lowercase)
    key = key.lower()
    key_alphabet = CreateAlphabet(key,default_alph_shift=0)
    ciphertext = ""
    for letter in plaintext:
        if letter not in default_alphabet:
            ciphertext += letter
        else:
            ciphertext += key_alphabet[default_alphabet.index(letter)]
    return ciphertext

def KeywordSubstitutionDecode(ciphertext,key,default_alph_shift=0):
    default_alphabet = list(string.ascii_lowercase)
    key_alphabet = CreateAlphabet(key,default_alph_shift)
    plaintext = ""
    for letter in ciphertext:
        if letter not in default_alphabet:
            plaintext += letter
        else:
            plaintext += default_alphabet[key_alphabet.index(letter)]
    return plaintext
