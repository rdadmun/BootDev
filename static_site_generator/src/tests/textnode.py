from enum import Enum

class TextType:
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text: str, text_type: str = TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)                   
        return False
    
    def __repr__(self):
        return "fTextNode({self.text}, {self.text_type.value}, {self.url})"