def user_words(initial_words):
    words = initial_words

    def add_word(word):
        nonlocal words
        words = words + (word,)
        return words

    return add_word
