import random
from string import ascii_lowercase, ascii_uppercase

LOWER_ALPHA = ascii_lowercase
UPPER_ALPHA = ascii_uppercase
FULL_ALPHA = LOWER_ALPHA + UPPER_ALPHA
ALPHA_DIGITS = FULL_ALPHA + "0123456789"


def shift(character: str, shift: int) -> str:
    """Shifts a single character along the alphabet"""
    # Checking if character is lowercase, uppercase or not a letter
    if character in LOWER_ALPHA:
        temp_alpha = LOWER_ALPHA
    elif character in UPPER_ALPHA:
        temp_alpha = UPPER_ALPHA
    else:
        return character

    location = temp_alpha.index(character)
    character = temp_alpha[(location + shift) % 26]
    return character


def caesar(plain_text: str, key: int) -> str:
    """Performs the caesar chipher on a string given a key"""
    cipher_text = ""
    for char in plain_text:
        cipher_text += shift(char, key)
    return cipher_text


def neighbour_swap(plain_text: str) -> str:
    """Swaps adjacent characters in pairs. Eg: \"PYTHON\" > \"YPHTNO\""""
    plain_text = list(plain_text)
    symbols = []

    # removing symbols and storing their location
    for index in range(len(plain_text)):
        if not(plain_text[index] in ALPHA_DIGITS):
            symbols.append([index, plain_text[index]])
            plain_text[index] = "@"  # maintains string length so subsequent loops aren't messed up

    plain_text = [char for char in plain_text if char != "@"]  # removing the "@"s

    for index in range(1, len(plain_text), 2):  # Goes through every pair of characters
        # Assigns both simultaneously as both read from eachother
        plain_text[index - 1], plain_text[index] = plain_text[index], plain_text[index - 1]

    # Adding symbols back to final string
    for element in symbols:
        plain_text.insert(element[0], element[1])

    return "".join(plain_text)


def random_substitution(plain_text: str, seed: int) -> str:
    """Encodes a string using a substitution cipher generated from the seed"""
    lower_shuffle = list(LOWER_ALPHA)
    upper_shuffle = list(UPPER_ALPHA)
    random.seed(seed)  # makes randomization always the same for a specific seed
    random.shuffle(lower_shuffle)
    random.seed(seed)
    random.shuffle(upper_shuffle)
    # Dictionary for encoding the string, eg. {"a": "u", "b": "e" ...}
    # zip() is used to combine two iterables into one
    cipher = {letter: randLetter for letter, randLetter in zip(FULL_ALPHA, lower_shuffle + upper_shuffle)}
    cipher_text = ""
    for char in plain_text:
        if char in list(FULL_ALPHA):
            cipher_text += cipher[char]
        else:
            cipher_text += char
    return cipher_text
