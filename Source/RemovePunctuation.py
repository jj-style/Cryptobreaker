import string

punctuation = string.punctuation + "’" + '“' + "‘" + "—"

def RemovePunctuation(text,remove_spaces=True,to_lower=True):
    text = list(text)
    while "\n" in text:
        text.remove("\n")
    text = "".join(text)
    if remove_spaces:
        text = text.replace(" ","")
    if to_lower:
        text=text.lower()
    for letter in text:
        if letter in punctuation:
            text = text.replace(letter,"")
    text = text.strip("\n")
    return text
