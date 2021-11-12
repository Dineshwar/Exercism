def is_isogram (string):
    string = string.lower()
    for c in string:
        if c.isalpha() and string.count(c)>1:
            return False
    return True
