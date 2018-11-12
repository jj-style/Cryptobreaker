import pickle


#Returns a frequency distribution
def findBigrams(text):
    text = text.lower()
    text = removeSpaces(text)
    bigrams = {}
    total = 0
    for i in range(97,123):
        for j in range(97,123):
            bigrams[chr(i)+chr(j)] = 0
    for i in range(len(text)-1):
        bigram = text[i:i+2]
        bigrams[bigram] += 1
        total += 1
    for i in range(97,123):
        for j in range(97,123):
            bigrams[chr(i)+chr(j)] = bigrams[chr(i)+chr(j)]/total
    return bigrams

def checkLetter(n):
    if ord(n.lower()) >= 97 and ord(n.lower()) <= 124:
        return True
    else:
        return False
    
def letterToNumber(n):
    if ord(n) >= 97:
        return ord(n) - 97
    else:
        return ord(n) - 65
    
def numberToLetter(n):
    return chr(n+97)

def removeSpaces(text):
    i = 0
    newText = ""
    while i < len(text):
        if  ord(text[i]) < 123 and ord(text[i]) > 96:
            newText = newText + text[i]
        i+=1
    return newText

def saveBigramDistribution(bigrams):
    pickle_out = open("dict.pickle","wb")
    pickle.dump(bigrams,pickle_out)
    pickle_out.close()

def openBigramDistribution():
    pickle_in = open("dict.pickle","rb")
    bigrams = pickle.load(pickle_in)
    return bigrams

#Get the x squared value of the text compared to the standard English distribution for the Chi Squared statistical test
def getxSquared(text):
    textDistribution = findBigrams(text)
    xSquared = 0
    for i in range(97,123):
        for j in range(97,123):
            key = chr(i)+chr(j)
            try:
                xSquared += ((textDistribution[key] - standard[key])**2)/standard[key]
            except ZeroDivisionError:
                continue
    return xSquared

#checks whether text is in English/other similar language. E.g. Latin
#Only works reliably for text longer than roughly 1500 characters. Ideally longer than 2000.
def checkEnglish(text):
    xSquared = getxSquared(text)
    if len(text) < 2000:
        if  xSquared < 3*34.71*(len(text)**(-0.467)):
            return True
        else:
            return False
    else:
        if xSquared < 1:
            return True
        else:
            return False
        
#Opens the standard bigram distribution    
standard = openBigramDistribution()
