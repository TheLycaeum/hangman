import random

def choose_word(fname):
    good_words = []

    f = open(fname)
    for i in f:
        i = i.strip()
        if i.islower() and i.isalpha() and len(i) >= 6:
            good_words.append(i)
    f.close()
    
    return random.sample(good_words, 1)[0]

    
    
