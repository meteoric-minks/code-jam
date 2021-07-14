import random
from string import ascii_lowercase


def shift(character: str, shift: int) -> str:
    """Shifts a single character along the alphabet"""
    if character == " ":
        return character
    location = ascii_lowercase.index(character)
    character = ascii_lowercase[(location + shift) % 26]
    return character


def caesar(plainText: str, key: int) -> str:
    """Performs the caesar chipher on a string given a key"""
    cipherText = ""
    for char in plainText.lower():
        cipherText += shift(char, key)
    return cipherText


def pairSwapper(plainText: str) -> str:
    """Swaps adjacent characters in pairs. Eg: \"PYTHON\" > \"YPHTNO\""""
    #  This was stolen from a previous project of mine, so sorry if it's hard to read
    for index in range(1, len(plainText), 2):  # Goes through every pair of characters
        # Assigns both simultaneously as both read from eachother
        plainText[index - 1], plainText[index] = plainText[index], plainText[index - 1]
    return plainText


def randomSwapper(plainText: str, seed: int) -> str:
    """Encodes a string using a randomly generated substitution cipher (the same seed will use the same cipher)"""
    random.seed(seed)  # makes randomization always the same for a specific seed
    shuffledAlphabet = random.shuffle(ascii_lowercase)
    # Dictionary for encoding the string, eg. {"a": "u", "b": "e" ...}
    # zip() is used to combine two iterables into one
    cipher = {letter: randLetter for letter, randLetter in zip(ascii_lowercase, shuffledAlphabet)}
    cipherText = ""
    for char in plainText:
        cipherText += cipher[char]
    return cipherText
