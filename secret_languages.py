import validators
from string import punctuation

# consonants not including 'y'
CONSONANTS = "bcdfghjklnmpqrstvwxz"

LANGUAGES = ["piglatin"]


def word_to_pig_latin(word):
    """Converts an English word to Pig Latin.

    Args:
        word (string): A string in English to convert to Pig Latin

    Returns:
        [string]: A word in Pig Latin
    """

    # if word is not only letters, return the word as is
    if not word.isalpha():
        return word

    new_word = word.lower()
    to_append = ""
    for index, letter in enumerate(word.lower()):
        # if there are consonants at the beginning of the word,
        # take them out to be added to the end of the word later
        if letter in CONSONANTS or (letter == "y" and index == 0):
            new_word = new_word[1:]
            to_append += letter

        # when the letter hits a vowel,
        # add the pig latin ending "yay" or "ay"
        if letter not in CONSONANTS:
            if to_append:
                to_append += "ay"
            else:
                to_append = "yay"
            break

    return new_word + to_append


def translate_word(word, language="piglatin"):
    # keep any punctuation at the start of the word
    # to add to the start of the translation
    start_punctuation = ""
    for index, char in enumerate(word):
        if char in punctuation:
            start_punctuation += char

            # if the word is just punctuation,
            # return it as is
            if index == len(word) - 1:
                return word
        else:
            break

    # keep any punctuation at the end of the word
    # to add the end of the translation
    end_punctuation = ""
    for char in reversed(word):
        if char in punctuation:
            end_punctuation = char + end_punctuation
        else:
            break

    translation = word

    if language == "piglatin":
        translation = word_to_pig_latin(word.strip(punctuation))

    # if the word was capitalized, keep it that way
    if word.strip(punctuation) == word.strip(punctuation).capitalize():
        translation = translation.capitalize()

    # if the word was all upper case, keep it that way
    if word.strip(punctuation) == word.strip(punctuation).upper():
        translation = translation.upper()

    return start_punctuation + translation + end_punctuation


def translate_text(text, language="piglatin", keep_usernames=True, keep_hashtags=True):
    split_text = text.split()
    new_text = ""
    for word in split_text:
        # if usernames shouldn't be translated
        # and the word begins with an @, return as is
        if keep_usernames and word[0] == "@":
            new_text += word + " "
        elif keep_hashtags and word[0] == "#":
            new_text += word + " "
        # if the word is a url, return it as is
        elif validators.url(word):
            new_text += word + " "
        else:
            new_text += translate_word(word, language=language) + " "

    return new_text.strip()
