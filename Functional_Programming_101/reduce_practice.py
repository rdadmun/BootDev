import functools

def join(doc_so_far, sentence):
    sentences = doc_so_far + sentence
    return sentences

def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(lambda a, b: a + ". " + b,sentences[:n]) + "."