def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = [convert_md_to_txt(arg) for arg in args]
        converted_kwargs = {key: convert_md_to_txt(value) for key, value in kwargs.items()}
        return func(*converted_args, **converted_kwargs)
    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)