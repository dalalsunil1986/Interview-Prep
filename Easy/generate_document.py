from collections import Counter

"""
Very simple solution using built in libraries to just count up
occurrences and ensure that we have at least the needed number of chars
in our string to generate the document, based on chars and counts in
the document. 
"""


def generateDocument(characters, document):
    avail_chars = Counter(characters)
    needed_chars = Counter(document)
    for needed_char in document:
        if avail_chars.get(needed_char, 0) < needed_chars[needed_char]:
            return False

    return True


"""
Basically the same as sol1 except we use 1 dict (less space) and less time
but asymptotically the same O(m + n) 
"""


def generateDocument(characters, document):
    char_cts = {}
    for char_avail in characters:
        char_cts[char_avail] = char_cts.get(char_avail, 0) + 1

    for needed_char in document:
        # if char isn't in our dict or freq for needed_char = 0 we can't make doc.
        if needed_char not in char_cts or not char_cts[needed_char]:
            return False

        # decrement each time we encounter the char, if it hits 0 and we still
        # have that character in the document, we don't have enough of this char to
        # create doc.
        char_cts[needed_char] -= 1

    return True
