import string

from IndexOfCoincidence import *
from DetectEnglish import *

from KeywordSubstitution import *
from Vigenere import *
from Beaufort import *
from Autokey import *
from Playfair import *

def ReadFile(filename):
    words = []
    with open(filename,'r') as file:
        for row in file:
            words.append(row.strip())
    return words

english_words = ReadFile('english_words.txt')

def BruteforceDictionaryAttack(ciphertext,cipher_name,german=False,alph_shift=0):
    key_length = GetKeyLength(ciphertext)
    key_length_dependent = ["Vigenere","Beaufort"]
    for word in english_words:
        if cipher_name not in key_length_dependent:
            if cipher_name == "Keyword Substitution":
                plaintext = KeywordSubstitutionDecode(ciphertext,word,default_alph_shift=alph_shift)
            elif cipher_name == "Autokey":
                plaintext = AutokeyDecode(ciphertext,word)
            elif cipher_name == "Playfair":
                plaintext = PlayfairDecode(ciphertext,word)
        else:
            plaintext = "zzzzz"
            if len(word) in range(key_length-1,key_length+1):
                if cipher_name == "Vigenere":
                    plaintext = VigenereDecode(ciphertext,word)
                elif cipher_name == "Beaufort":
                    plaintext = BeaufortDecode(ciphertext,word,german)
                #POLYAFFINE - how does keyword map to keys???
        if checkEnglish(plaintext) == True:
            return plaintext,word
    return "Cipher could not be broken using a dictionary attack","Key not found"
