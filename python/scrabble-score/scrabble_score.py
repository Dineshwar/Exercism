def score(word):
    count = 0
    my_dict = dict.fromkeys(['a', 'e', 'i','o','u','l','n','r','s','t'], 1)
    my_dict.update(dict.fromkeys(['d', 'g'], 2))
    my_dict.update(dict.fromkeys(['b', 'c', 'm', 'p'], 3))
    my_dict.update(dict.fromkeys(['f', 'h', 'v', 'w', 'y'], 4))
    my_dict.update(dict.fromkeys(['k'], 5))
    my_dict.update(dict.fromkeys(['j', 'x'], 8))
    my_dict.update(dict.fromkeys(['q', 'z'], 10))
    new_word = word.lower()
    for c in new_word:
        if c in my_dict:
            count+=my_dict[c]
    return count
	
