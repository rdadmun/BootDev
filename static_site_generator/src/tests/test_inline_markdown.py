import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, text_type_bold, text_type_code, text_type_text, text_type_italic, text_type_link, text_type_image, text_node_to_html_node

class TestInlineMardown(unittest.TestCase):

    def test_no_markdown(self):
        node_1 = TextNode("this has no markdown", text_type_text)
        node_2 = TextNode("neither does this text", text_type_text)
        new_nodes = split_nodes_delimiter([node_1, node_2], "**", text_type_bold)
        self.assertEqual(new_nodes, [TextNode("this has no markdown", text_type_text), TextNode("neither does this text", text_type_text)])

    def test_delim_bold(self):
        node_1 = TextNode("this text has **bold** in it", text_type_text)
        new_nodes = split_nodes_delimiter([node_1], "**", text_type_bold)
        self.assertEqual(new_nodes, [TextNode("this text has ", text_type_text), TextNode("bold", text_type_bold), TextNode(" in it", text_type_text)])

    def test_delim_bold_mult(self):
        node1 = TextNode("this text has **bold** text in it **two times** yeah?", text_type_text)
        new_nodes = split_nodes_delimiter([node1], "**", text_type_bold)
        self.assertEqual(new_nodes, 
                         [
                             TextNode("this text has ", text_type_text), 
                             TextNode("bold", text_type_bold), 
                             TextNode(" text in it ", text_type_text),
                             TextNode("two times", text_type_bold),
                             TextNode(" yeah?", text_type_text)
                             ]
                             )
        
    def test_delim_code(self):
        node1 = TextNode("this text has `a code block` in it", text_type_text)
        new_nodes = split_nodes_delimiter([node1], "`", text_type_code)
        self.assertEqual(new_nodes, [TextNode("this text has ", text_type_text), TextNode("a code block", text_type_code), TextNode(" in it", text_type_text)])
    
    def test_delim_italic(self):
        node_1 = TextNode("this text has *italic* in it", text_type_text)
        new_nodes = split_nodes_delimiter([node_1], "*", text_type_italic)
        self.assertEqual(new_nodes, [TextNode("this text has ", text_type_text), TextNode("italic", text_type_italic), TextNode(" in it", text_type_text)])

    def test_delim_bold_and_italic(self):
        node_1 = TextNode("this text has **bold text** and *italic text* in it", text_type_text)
        new_nodes = split_nodes_delimiter([node_1], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("this text has ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("italic text", text_type_italic),
            TextNode(" in it", text_type_text)
        ])
        
if __name__ == "__main__":
    unittest.main()