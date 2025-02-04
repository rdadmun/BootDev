from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    if from_format == DocFormat.MD and to_format == DocFormat.HTML:
        if content.startswith('#'):
            return f"<h1>{content[1:].strip()}</h1>"
    
    if from_format == DocFormat.TXT and to_format == DocFormat.PDF:
        return f"[PDF] {content} [PDF]"
    
    if from_format == DocFormat.HTML and to_format == DocFormat.MD:
        if content.startswith('<h1>'):
            return f"# {content.lstrip('<h1>').rstrip('</h1>')}"
    else:
        raise Exception('Invalid type')