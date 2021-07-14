from string import ascii_lowercase


def shift(character: str, shift: int):
    """Shifts a single character along the alphabet"""
    character.lower()
    location = ascii_lowercase.index(character)
    character = ascii_lowercase[(location + shift) % 26]


def caesar(plainText: str, key: int):
    """Performs the caesar chipher on a string given a key"""
    cipherText = ""
    for char in plainText:
        cipherText += shift(char, key)
