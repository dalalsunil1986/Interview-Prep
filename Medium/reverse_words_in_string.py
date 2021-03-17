def reverseWordsInString(string):
    """
    Simply use 2 pointer technique to iterate through the string, appending each word in the string to the output
    array, and if we encounter whitespace, address w/ 2nd nested while loop and keep using string slicing to append
    up to but not including the j^{th} index, and move i along the string. Then use list comp of iterating from end
    of list to beginning to join words and whitespaces in reverse order. Could also use a helper method and swap end
    with beginning (again 2 pointer) to reverse the words list before returning. Wrote helper method for practice, but
    no need to use since we are using O(n) space in the best case either way for the output array, the additional list
    from the list comp wouldn't change asymptotic space complexity.

    Method runs in O(n) time since we only iterate through string once, and append is average O(1), uses O(n) space
    :param string: input string that may or may not be empty.
    :return: reversed version (words and whitespace, may be multiple whitespaces between words) of input string
    """
    i = j = 0
    n, WHITE_SPACE = len(string), ' '
    words = []
    while i < n:
        while j < n and string[j] != WHITE_SPACE:
            j += 1
        words.append(string[i: j])
        # move i to where j is (first whitespace)
        i = j
        # address whitespace case
        while j < n and string[j] == WHITE_SPACE:
            j += 1
        words.append(string[i: j])
        i = j
    # iterate backwards through list, append each word/whitespace to new list and join them
    return "".join([words[word] for word in range(len(words) - 1, -1, -1)])

    # since [::-1] could be considered a "built in" reverse method.
    # return "".join(words[::-1])


def reverse_words_list(words):
    """
    Helper method
    :param words: original words from input string separated into list
    :return: none
    """
    i, j = 0, len(words) - 1
    while i < j:
        words[i], words[j] = words[j], words[i]
