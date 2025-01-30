def toggle_case(line):
    if line.istitle():
        pass
    if line.isupper():
        pass
    if len(line) > 0 and line[1:].islower():
        pass
    else:
        return line