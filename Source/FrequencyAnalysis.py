import string

alphabet = list(string.ascii_lowercase)

def FrequencyAnalysis(text):
    analysis = []
    for letter in alphabet:
        analysis.append([letter,0])
    
    for letter in text:
        if letter in alphabet:
            analysis[alphabet.index(letter)][1] += 1
    return analysis

def LetterFrequencyAnalysis(text):
    most_common = 'etaoinshrdlcumwfgypbvkjxqz'
    letter_freq = {}
    for letter in text:
        if letter in alphabet:
            if letter not in letter_freq:
                letter_freq[letter] = 1
            else:
                letter_freq[letter] += 1
    for letter in alphabet:
        if letter not in letter_freq:
            letter_freq[letter] = 0
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda x: x[1],reverse=True)
    return sorted_letter_freq
