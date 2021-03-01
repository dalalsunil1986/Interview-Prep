"""
The idea is just to map each char to it's decimal value (ASCII style) and then if the number of shifts (key) plus the
current decimal representation of the character is > dec(z) = 122, we just wrap it back around from 'a'.

I.e., if letter = 'z' and k = 53 then 53 % 26 = 1 and 122 + 1 = 123 so that is exactly 1 away from 'z' or can be
seen as 123-26 = 97 = 'a' so it wraps back around to 'a'.
"""


# O(n) time, O(n) space
def caesarCipherEncryptor(string, key):
    as_list = list(string)
    for idx, letter in enumerate(as_list):
        as_list[idx] = char_map(letter, key)
    return "".join(as_list)


def char_map(char, key):
    # 26 letters in alphabet
    value = ord(char) + (key % 26)
    # if within ASCII range ret. char otherwise wrap back around.
    return chr(value) if value <= 122 else chr((value - 26))
