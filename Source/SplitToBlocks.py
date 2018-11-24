def Blocks(n,text):
    blocks = [[] for i in range(n)]
    temp_text = list(text)
    while "\n" in temp_text:
            temp_text.remove("\n")
    text = "".join(temp_text)
    for i in range(len(text)):
        blocks[i%n].append(text[i])
    return blocks

def ShowBlocks(blocks):
    for b in blocks:
        print("".join(b))
        print("")
        
def ReconstructBlocks(blocks):
    text = ""
    for i in range(len(blocks[0])):
        for block in blocks:
            try:
                text += block[i]
            except:
                pass
    #print(text)
    return text

def ReconstructColumns(columns):
    text = ""
    for col in columns:
        text += "".join(col)
    return text

def SplitToColumns(ciphertext,key_length):
    columns = [[None for x in range(len(ciphertext)//key_length)] for i in range(key_length)]
    count = 0
    col_index = 0
    for letter in ciphertext:
        if None in columns[count]:
            columns[count][col_index] = letter
            col_index += 1
        else:
            count += 1
            col_index = 0
            columns[count][col_index] = letter
            col_index += 1
    return columns
