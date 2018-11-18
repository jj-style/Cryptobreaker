import string

alphabet = list(string.ascii_lowercase)

def RailfenceEncode(text,number_of_rows,from_bottom=False,return_as_text=True):
    ciphertext = ""
    row_choice = []
    for i in range(number_of_rows):
        row_choice.append(i)
    for i in range(number_of_rows-2,0,-1):
        row_choice.append(i)
    row_count = 0
    rows = [[] for i in range(number_of_rows)]
    for letter in text:
        rows[row_choice[row_count]].append(letter)
        row_count = (row_count + 1) % len(row_choice)
    if return_as_text:
        if not from_bottom:
            for row in rows:
                ciphertext += "".join(row)
        else:
            for i in range(len(rows)-1,-1,-1):
                ciphertext += "".join(rows[i])
    else:
        ciphertext = rows
    return ciphertext

def RailfenceDecode(text,number_of_rows):
    template = RailfenceEncode("x"*len(text),number_of_rows,return_as_text=False)
    rows = [[] for i in range(number_of_rows)]
    text_copy = text
    for i in range(number_of_rows):
        rows[i] = list(text_copy[:len(template[i])])
        text_copy = text_copy[len(template[i]):]
    plaintext = ""
    row_choice = []
    for i in range(number_of_rows):
        row_choice.append(i)
    for i in range(number_of_rows-2,0,-1):
        row_choice.append(i)
    row_count = 0
    for i in range(len(text)):
        try:
            plaintext += rows[row_choice[row_count]].pop(0)
            row_count = (row_count + 1) % len(row_choice)
        except:
            row_count = (row_count + 1) % len(row_choice) 
    return plaintext
