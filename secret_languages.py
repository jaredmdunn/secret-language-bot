from string import punctuation

CONSONANTS = "bcdfghjklnmpqrstvwxyz"


def word_to_pig_latin(word):
    """Converts an English word to Pig Latin.

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
        # if there is punctuation at the beginning of word,
        # take them out to be added to the front of the word later
        if letter in punctuation:
            new_word = new_word[1:]
            to_prepend += letter

        # if there are consonants at the beginning of the word,
        # take them out to be added to the end of the word later
        if letter in CONSONANTS:
            new_word = new_word[1:]
            to_append += letter

        # when the letter hits a vowel (or the end of the word),
        # add the pig latin ending "yay" or "ay"
        if (
            letter not in CONSONANTS
            and letter not in punctuation
            or index == len(word) - 1
        ):
            if not to_append and (index == 0):
                to_append = "yay"
            else:
                to_append += "ay"
            break
    # take off any punctuation on the end to be appended later
    for letter in reversed(word.lower()):
        if letter in punctuation:
            new_word = new_word[:-1]
            to_append += letter
        else:
            break

    new_word += to_append
    # if the word was capitalized, keep it that way
    if word == word.capitalize():
        new_word = new_word.capitalize()
    # if the word was all upper case, keep it that way
    if word == word.upper():
        new_word == new_word.upper()
    return new_word


def text_to_pig_latin(text):
    split_text = text.split()
    new_text = ""
    for word in split_text:
        new_text += word_to_pig_latin(word) + " "
    return new_text.strip()
