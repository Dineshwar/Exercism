"""Little Sister's Vocabulary From exercism to learn String Functions."""
def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return "un" + word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    return ' :: '.join(vocab_words[0] + val if i != 0 else vocab_words[0] for i, val in enumerate(vocab_words))


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    word = replace_last(word, 'ness', '')
    return word if word[-1] != 'i' else word[:-1] + 'y'


def noun_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    sentence_list = sentence.split()
    return sentence_list[index].replace('.', '') + 'en'

def replace_last(string, find, replace):
    """

    :param string: str the word with need to be replaced
    :param find:  str the find string
    :param replace:  str the replace string
    :return:  str word that changes the extracted adjective to a verb.

    This function takes `string`, `find` and `replace`
    will reverse the `string` , `find` and `replace` replace the `find` with `replace` in first occurrence.
    """
    reversed = string[::-1]
    replaced = reversed.replace(find[::-1], replace[::-1], 1)
    return replaced[::-1]
