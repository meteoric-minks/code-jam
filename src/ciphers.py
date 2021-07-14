import random
from string import ascii_lowercase, ascii_uppercase

LOWER_ALPHA = ascii_lowercase
UPPER_ALPHA = ascii_uppercase
FULL_ALPHA = LOWER_ALPHA + UPPER_ALPHA
ALPHA_DIGITS = FULL_ALPHA + "0123456789"


def shift(character: str, shift: int) -> str:
    """Shifts a single character along the alphabet"""
    if character in LOWER_ALPHA:
        temp_alpha = LOWER_ALPHA
    elif character in UPPER_ALPHA:
        temp_alpha = UPPER_ALPHA
    else:
        return character

    location = temp_alpha.index(character)
    character = temp_alpha[(location + shift) % 26]
    return character


def caesar(plainText: str, key: int) -> str:
    """Performs the caesar chipher on a string given a key"""
    cipherText = ""
    for char in plainText:
        cipherText += shift(char, key)
    return cipherText


def pairSwapper(plainText: str) -> str:
    """Swaps adjacent characters in pairs. Eg: \"PYTHON\" > \"YPHTNO\""""
    plainText = list(plainText)
    symbols = []

    # removing symbols and storing their location
    for index in range(len(plainText)):
        if not(plainText[index] in ALPHA_DIGITS):
            symbols.append([index, plainText[index]])
            plainText[index] = "@"  # maintains string length so subsequent loops aren't messed up

    plainText = [char for char in plainText if char != "@"]  # removing the "@"s

    for index in range(1, len(plainText), 2):  # Goes through every pair of characters
        # Assigns both simultaneously as both read from eachother
        plainText[index - 1], plainText[index] = plainText[index], plainText[index - 1]

    # Adding symbols back to final string
    for element in symbols:
        plainText.insert(element[0], element[1])

    return "".join(plainText)


def randomSubstitute(plainText: str, seed: int) -> str:
    """Encodes a string using a randomly generated substitution cipher (the same seed will use the same cipher)"""
    lowerShuffle = list(LOWER_ALPHA)
    upperShuffle = list(UPPER_ALPHA)
    random.seed(seed)  # makes randomization always the same for a specific seed
    random.shuffle(lowerShuffle)
    random.seed(seed)
    random.shuffle(upperShuffle)
    # Dictionary for encoding the string, eg. {"a": "u", "b": "e" ...}
    # zip() is used to combine two iterables into one
    cipher = {letter: randLetter for letter, randLetter in zip(FULL_ALPHA, lowerShuffle + upperShuffle)}
    cipherText = ""
    for char in plainText:
        if char in list(FULL_ALPHA):
            cipherText += cipher[char]
        else:
            cipherText += char
    return cipherText
