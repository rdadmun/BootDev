def file_type_getter(file_extension_tuples):
    file_extension_dict = {}
    for file_type, extensions in file_extension_tuples:
        for extension in extensions:
            file_extension_dict[extension] = file_type
    return lambda ext: file_extension_dict.get(ext, "Unknown")
    