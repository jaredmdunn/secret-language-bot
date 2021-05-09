CONSONANTS = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "n",
    "m",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def word_to_pig_latin(word):
    new_word = word
    to_append = ""
    for index, letter in enumerate(word.lower()):
        if letter in CONSONANTS:
            new_word = new_word[1:]
            to_append += letter
        else:
            if index == 0:
                to_append = "yay"
            else:
                to_append += "ay"
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
    return new_text
