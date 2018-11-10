import string
from SplitToBlocks import Blocks
from RemovePunctuation import *

alphabet = string.ascii_lowercase

def IOC(text):
    text = RemovePunctuation(text)
    letter_count = {}
    for letter in text:
        if letter in alphabet:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    ioc = 0
    length = len(text)
    for count in letter_count:
        frequency = letter_count[count]
        ioc += ((frequency*(frequency-1)) / (length*(length-1)))
    return ioc

def CalculateKeyLength(text):
    text = RemovePunctuation(text)
    probable_key_lengths = []
    for i in range(1,26):
        blocks = Blocks(i,text)
        average_ioc = 0
        for block in blocks:
            blocki_ioc = IOC("".join(block))
            average_ioc += blocki_ioc
        average_ioc /= i
        if average_ioc > 0.059 and average_ioc < 0.071:
            probable_key_lengths.append([i,average_ioc])

    for prob_key in probable_key_lengths:
        print("Key length {}  IOC {}".format(prob_key[0],prob_key[1]))
    return probable_key_lengths

