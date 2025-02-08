import unittest
from textnode import TextNode, text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)
    
    def test_url_eq(self):
        node = TextNode("This is a text node", text_type_bold, "https://bottdev.com")
        node2 = TextNode("This is a text node", text_type_bold, "https://bottdev.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", text_type_bold, "https://bottdev.com")
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_text_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is another text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html(self):
        text_node = TextNode("text", text_type_text)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, "text"))
        
        bold_node = TextNode("text", text_type_bold)
        self.assertEqual(text_node_to_html_node(bold_node), LeafNode("b", "text"))

        italic_node = TextNode("text", text_type_italic)
        self.assertEqual(text_node_to_html_node(italic_node), LeafNode("i", "text"))
        
        code_node = TextNode("text", text_type_code)
        self.assertEqual(text_node_to_html_node(code_node), LeafNode("code", "text"))

        link_node = TextNode("text", text_type_link, "boot.dev")
        self.assertEqual(text_node_to_html_node(link_node), LeafNode("a", "text", {"href": "boot.dev"}))
        
        image_node = TextNode("text", text_type_image, "image.com")
        self.assertEqual(text_node_to_html_node(image_node), LeafNode("img", "", {"src": "image.com", "alt": "text"}))

        with self.assertRaises(Exception) as context:
            unsupported_type = TextNode("text", None)
            text_node_to_html_node(unsupported_type)
        self.assertEqual(str(context.exception), "None text type unsupported")

if __name__ == "__main__":
    unittest.main()