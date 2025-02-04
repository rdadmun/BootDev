def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        if option == "--one":
            return filter_one(content)
        if option == "--two":
           return filter_two(content)
        if option == "--three":
            return filter_two(filter_one(content))
        else:
            return "invalid option"
    return filter_cmd

# OR

def get_filter_cmd_2(filters):
    def filter_cmd(content, options, word_pairs):
        if len(options) == 0:
            raise Exception("missing options")
        for option in options:
            if option in filters:
                content = filters[option](content, word_pairs)
            else:
                raise Exception("invalid option")
        return content

    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
