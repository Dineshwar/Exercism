def abbreviate(words):
    try:
        sp = (words.replace('-',' ').replace('_','')).split()
        return ''.join([c[0] for c in sp]).upper()
    except:
        return "Error Occur"
