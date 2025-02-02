from functools import reduce

def lineator(line_length):
    def lineate(document):
        words = document.split()

        def add_word_to_lines(lines, word):
            if len(lines) == 0:
                lines.append(word)
            else:
                if len(lines[-1]) + len(word) + 1 > line_length:
                    lines.append(word)
                else:
                    lines[-1] += " " + word
            return lines
            
        return reduce(add_word_to_lines, words, [])

    return lineate
