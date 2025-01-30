def remove_invalid_lines(document):
    removed = list(filter(lambda line: not line.startswith("-"), document.split("\n")))
    return "\n".join(removed)

#OR

def remove_invalid_lines_2(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )


