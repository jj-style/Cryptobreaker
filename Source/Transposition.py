import string
from DetectEnglish import *
from SplitToBlocks import *

alphabet = list(string.ascii_lowercase)

def TranspositionEncode(text,keyword):
    ciphertext = ""
    split_text = Blocks(len(keyword),text)
    grid = []
    for i in range(len(keyword)):
        grid.append([[i,keyword[i]],split_text[i]])
    grid = sorted(grid,key=lambda x: x[0][1])
    ciphertext_grid = []
    for i in range(len(keyword)):
        ciphertext_grid.append(grid[i][1])
    print(ReconstructBlocks(ciphertext_grid))
    return ciphertext

def TranspositionDecode(ciphertext,key,to_upper=False):
    plaintext = ""
    return plaintext
           

TranspositionEncode('helloworld','key')
