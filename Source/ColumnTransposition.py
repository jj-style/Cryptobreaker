import string
from SplitToBlocks import *

alphabet = list(string.ascii_lowercase)

def TranspositionEncode(text,keyword,regular=False,by_column=False):
    ciphertext = ""
    if not keyword.isalpha():
        keyword = list(map(int,keyword.split(",")))
    if regular:
        text += ((len(keyword)-1)%len(text))*"x"
    if not by_column:
        split_text = Blocks(len(keyword),text)
    else:
        split_text = SplitToColumns(ReconstructColumns(SplitToColumns(text,len(keyword))))
    grid = []
    for i in range(len(keyword)):
        grid.append([[i,keyword[i]],split_text[i]])
    grid = sorted(grid,key=lambda x: x[0][1])
    ciphertext_grid = []
    for i in range(len(keyword)):
        ciphertext_grid.append(grid[i][1])
    ciphertext = ReconstructBlocks(ciphertext_grid)
    return ciphertext

def TranspositionDecode(text,keyword,by_column=False):
    return TranspositionEncode(text,keyword,by_column)
