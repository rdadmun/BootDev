def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.splitlines()
            line_count = 0
            for line in lines:
                if sequence in line:
                    line_count += 1
            return line_count

        return with_length

    return with_char
