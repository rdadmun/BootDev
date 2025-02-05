from enum import Enum

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return (f"HTMLNode(tags={self.tag}, value={self.value}, "
                f"children={self.children}, props={self.props}")
        
    def text_node_to_html_node(text_node):
        def __init__(super):
            return ValueError
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children = [], props=props)
        
    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return self.value
        props_str = f' {self.props_to_html()}' if self.props else ''
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    SELF_CLOSING_TAGS = {'img', 'br', 'hr', 'input', 'meta', 'link'}
    
    def __init__(self, tag, children, props):
        super().__init__(tag=tag, value=[], children=children, props=props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        if self.children is None:
            raise ValueError("Children attribute cannot be None")
        if self.tag in self.SELF_CLOSING_TAGS:
            props_str = f' {self.props_to_html()}' if self.props else ''
            return f"<{self.tag}{props_str}/>"
        
        
        children_html = ''.join(child.to_html() if isinstance(child, HTMLNode) else child for child in self.children)
        
        props_str = f' {self.tag}{self.props_to_html()}' if self.props else ''
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
        
        
        