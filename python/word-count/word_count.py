import re

def count_words(sentence):
    s2 = sentence.lower()
    words = re.sub('[:!@#$._,&%^\n]', ' ', s2).split()
    new_words = []
    for word in words:
        word = re.sub(r"^'", '', word)
        word = re.sub(r"'$", '', word)
        new_words.append(word)
    return {s:new_words.count(s) for s in new_words}

