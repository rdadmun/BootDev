import unittest
from inline_markdown import text_to_text_nodes, split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link
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
        
        
    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extraction = extract_markdown_images(text)
        self.assertEqual(extraction, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extraction = extract_markdown_links(text)
        self.assertEqual(extraction, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_link_split(self):

        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
        ])

    def test_image_split(self):

        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", text_type_text),
            TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_text_to_nodes_delimiter_error(self):
        text = "This is **text with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
        with self.assertRaises(ValueError) as context:
            text_to_text_nodes(text)
        self.assertEqual(str(context.exception), "no closing delimiter found")

    def test_text_to_nodes_delimiter_error_italic(self):
        text = "This is **text** with an *italic word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
        with self.assertRaises(ValueError) as context:
            text_to_text_nodes(text)
        self.assertEqual(str(context.exception), "no closing delimiter found")

    def text_text_to_nodes_image_error(self):
        text = "This is text with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg and a [link](https://boot.dev)"
        text_to_text_nodes(text)
        self.assertRaises(ValueError)


if __name__ == "__main__":
    unittest.main()