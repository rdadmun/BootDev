def word_count_aggregator():
    w_c = 0
    def word_count(doc):
        nonlocal w_c
        w_c += len(doc.split())
        return w_c
    return word_count