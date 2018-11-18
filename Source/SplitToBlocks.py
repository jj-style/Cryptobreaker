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
    largest_block = len(blocks[0])
    for i in range(1,len(blocks)):
        if len(blocks[i]) > largest_block:
            largest_block = len(blocks[i])
    for i in range(largest_block):
        for block in blocks:
            try:
                text += block[i]
            except:
                pass
    return text
