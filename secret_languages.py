from string import punctuation

CONSONANTS = "bcdfghjklnmpqrstvwxyz"


def word_to_pig_latin(word):
    """Converts an English word to Pig Latin

    Args:
        word (string): A string in English to convert to Pig Latin

    Returns:
        [string]: A word in Pig Latin
    """

    # if the word is numeric, return it
    if word.strip(punctuation).isnumeric():
        return word

    new_word = word
    to_prepend = ""
    to_append = ""
    for index, letter in enumerate(word.lower()):
        if letter in punctuation:
            new_word = new_word[1:]
            to_prepend += letter

        if letter in CONSONANTS:
            new_word = new_word[1:]
            to_append += letter

        if letter not in CONSONANTS and letter not in punctuation:
            if index == 0:
                to_append = "yay"
            else:
                to_append += "ay"
            break
    for letter in reversed(word.lower()):
        if letter in punctuation:
            new_word = new_word[:-1]
            to_append += letter
        else:
            break

    new_word += to_append
    if word[0:1] == word[0:1].upper():
        new_word = new_word.capitalize()
    return new_word


def text_to_pig_latin(text):
    split_text = text.split()
    new_text = ""
    for word in split_text:
        new_text += word_to_pig_latin(word) + " "
    return new_text.strip()
