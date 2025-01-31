def find_longest_word(document, longest_word=""):
    if len(document) == 0:
        return longest_word
    words = document.split(maxsplit = 1)
    if len(words) == 0:
        return longest_word
    first_word = words[0]
    if len(first_word) > len(longest_word):
        longest_word = first_word
    if len(words) > 1:
        return find_longest_word(words[1], longest_word)
    return longest_word