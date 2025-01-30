default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    copy_commands = commands.copy()
    copy_commands[new_command] = function
    return copy_commands

def add_format(formats, format):
    copy_formats = formats.copy()
    copy_formats.append(format)
    return copy_formats

def save_document(docs, file_name, doc):
    copy_docs = docs.copy()
    copy_docs[file_name] = doc
    return copy_docs


def add_line_break(line):
    return line + "\n\n"
