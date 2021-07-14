from string import ascii_lowercase


def shift(character: str, shift: int) -> str:
    """Shifts a single character along the alphabet"""
    character.lower()
    location = ascii_lowercase.index(character)
    character = ascii_lowercase[(location + shift) % 26]
    return character


def caesar(plainText: str, key: int) -> str:
    """Performs the caesar chipher on a string given a key"""
    cipherText = ""
    for char in plainText:
        cipherText += shift(char, key)
    return cipherText
