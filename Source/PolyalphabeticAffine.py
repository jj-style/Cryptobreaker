import string

alphabet = list(string.ascii_lowercase)

def PolyAffineEncode(text,keys):
    ciphertext = ""
    for i in range(len(text)):
        key = keys[i%len(keys)]
        ciphertext += alphabet[((alphabet.index(text[i]) * key[0]) + key[1]) % len(alphabet)]
    return ciphertext

def inv(a): #inverts number -> x^-1
    return next(i for i in range(1,26) if (i*a) % 26 == 1)

def PolyAffineDecode(text,keys):
    plaintext = ""
    for i in range(len(text)):
        key = keys[i%len(keys)]
        plaintext += alphabet[((alphabet.index(text[i]) - key[1]) * inv(key[0])) % len(alphabet)]
    return plaintext
