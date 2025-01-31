def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(filename, content):
        file_extension = filename.split(".")[-1]
        if file_extension in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("Invalid file format")
    return inner_func
