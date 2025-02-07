import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

def text_to_text_nodes(text):
     nodes = [TextNode(text, text_type_text)]
     nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
     nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
     nodes = split_nodes_delimiter(nodes, "`", text_type_code)
     #nodes = split_nodes_image(nodes)
     #nodes = split_nodes_link(nodes)
     return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_node_list.append(node)
            continue
        split_nodes = []
        section = node.text.split(delimiter)

        if len(section) % 2 == 0:
            raise ValueError("no closing delimiter found")
        for i in range(len(section)):
            if section[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(section[i], text_type_text))
            else:
                split_nodes.append(TextNode(section[i], text_type))
        new_node_list.extend(split_nodes)
    return new_node_list