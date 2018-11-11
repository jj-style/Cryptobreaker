import string

alphabet = list(string.ascii_lowercase)

def AffineEncode(ciphertext,a,b):
    plaintext = ""
    for letter in ciphertext:
        if letter in alphabet:
            plaintext += alphabet[((alphabet.index(letter)*a) + b) % len(alphabet)]
        else:
            plaintext += letter
    return plaintext


def inv(a): #inverts number -> x^-1
    return next(i for i in range(1,26) if (i*a) % 26 == 1)

def AffineDecode(ciphertext,a,b,to_upper=False):
    plaintext = ""
    for letter in ciphertext:
        if letter not in alphabet:
            plaintext += letter
        else:
            plaintext += alphabet[(((alphabet.index(letter) - b) * inv(a)) % len(alphabet))]
    if to_upper == True:
        plaintext = plaintext.upper()
    return plaintext

def AffineBruteforce(ciphertext):
    plaintexts = []
    for i in range(26):
        for j in range(26):
            try:
                p = AffineDecode(ciphertext,i,j)
                plaintexts.append(p)
            except:
                pass
    return "\n\n".join(plaintexts)

##print(AffineEncode("hello",3,1))
##print(AffineDecode("wniir",3,1))
