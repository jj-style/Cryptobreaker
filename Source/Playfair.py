import string

playfair_matrix = [[0 for i in range(5)] for dimensions in range(5)]

def CreateAlphabet(key):
    default_alphabet = list(string.ascii_lowercase)
    default_alphabet.remove("j")
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

def ConvertTo2D(table):
    count = 0
    for i in range(5):
        for k in range(5):
            playfair_matrix[i][k] = table[count]
            count+=1

def PrepareMessage(pt):
    message = list(pt)
    while " " in message:
        message.remove(" ")
    message = [x for x in message if x]
    chunkedMessage = []
    tempListA = []
    tempListB = []
    for i in range(len(message)-2):
        if message[i] == message[i+1]:
            message.insert(i+1,"x")
    if len(message) % 2 != 0: message.append("x")
    for i in range(len(message)):
        if i % 2 == 0: tempListA.append(message[i])
        else: tempListB.append(message[i])
    for i in range(int(len(message)/2)):
        chunkedMessage.append(tempListA[i]+tempListB[i])
    return chunkedMessage

def findLetter(letter):
    i = 0
    k = 0
    while i < 5:
        while k < 5:
            if playfair_matrix[i][k] == letter:
                return i,k
            k+=1
        k = 0
        i+=1

def Erule1(x1,y1,x2,y2):
    try: c1 = playfair_matrix[x1][y1+1]
    except: c1 = playfair_matrix[x1][0]
    try: c2 = playfair_matrix[x2][y2+1]
    except: c2 = playfair_matrix[x2][0]
    return c1,c2

def Erule2(x1,y1,x2,y2):
    try: c1 = playfair_matrix[x1+1][y1]
    except: c1 = playfair_matrix[0][y1]
    try: c2 = playfair_matrix[x2+1][y2]
    except: c2 = playfair_matrix[0][y2]
    return c1,c2

def rule3(x1,y1,x2,y2):
    c1 = playfair_matrix[x1][y2]
    c2 = playfair_matrix[x2][y1]
    return c1,c2
    
def PrepareCipher(cipher):
    cipher = list(cipher)
    while " " in cipher:
        message.remove(" ")
    cipher = [x for x in cipher if x]
    chunkedCipher = []
    tempListA = []
    tempListB = []
    for i in range(len(cipher)):
        if i % 2 == 0: tempListA.append(cipher[i])
        else: tempListB.append(cipher[i])
    for i in range(int(len(cipher)/2)):
        chunkedCipher.append(tempListA[i]+tempListB[i])
    return chunkedCipher

def Drule1(x1,y1,x2,y2):
    try: c1 = playfair_matrix[x1][y1-1]
    except: c1 = playfair_matrix[x1][4]
    try: c2 = playfair_matrix[x2][y2-1]
    except: c2 = playfair_matrix[x2][4]
    return c1,c2

def Drule2(x1,y1,x2,y2):
    try: c1 = playfair_matrix[x1-1][y1]
    except: c1 = playfair_matrix[4][y1]
    try: c2 = playfair_matrix[x2-1][y2]
    except: c2 = playfair_matrix[4][y2]
    return c1,c2
    
def PlayfairEncode(plaintext,key):
    ConvertTo2D(CreateAlphabet(key))
    plaintext = PrepareMessage(plaintext)
    ciphertext = []
    while len(plaintext) > 0:
        pair = plaintext.pop(0)
        x1,y1 = findLetter(pair[0])
        x2,y2 = findLetter(pair[1])
        if x1 == x2:
            c1,c2 = Erule1(x1,y1,x2,y2)
        elif y1 == y2:
            c1,c2 = Erule2(x1,y1,x2,y2)
        else:
            c1,c2 = rule3(x1,y1,x2,y2)
        ciphertext.append(c1+c2)
    ciphertext = "".join(ciphertext)
    return ciphertext
    

def PlayfairDecode(ciphertext,key):
    ConvertTo2D(CreateAlphabet(key))
    ciphertext = PrepareCipher(ciphertext)
    plaintext = []
    while len(ciphertext) > 0:
        pair = ciphertext.pop(0)
        x1,y1 = findLetter(pair[0])
        x2,y2 = findLetter(pair[1])
        if x1 == x2:
            c1,c2 = Drule1(x1,y1,x2,y2)
        elif y1 == y2:
            c1,c2 = Drule2(x1,y1,x2,y2)
        else:
            c1,c2 = rule3(x1,y1,x2,y2)
        plaintext.append(c1+c2)
    plaintext = "".join(plaintext)
    return plaintext
