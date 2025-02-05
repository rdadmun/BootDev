import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        
    def test_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')
        
    def test_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_leaf_with_tag_and_value(self):
        node = LeafNode(tag="p", value = "Hello, world!", props = {"class": "text"})
        self.assertEqual(node.to_html(), '<p class="text">Hello, world!</p>')
        
    def test_leaf_with_tag_and_no_props(self):
        node = LeafNode(tag = "h1", value = "Welcome!", props = None)
        self.assertEqual(node.to_html(), '<h1>Welcome!</h1>')
        
    def test_leaf_with_tag(self):
        node = LeafNode(tag=None, value = "This is raw text", props = None)
        self.assertEqual(node.to_html(), "This is raw text")
        
    def test_leaf_with_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value = None, props = None)
            node.to_html()
            
    def test_leaf_with_empty_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="span", value = "", props = None)
            node.to_html()
            
    def test_leaf_with_props(self):
        node = LeafNode(tag="a", value="Click here", props = {"href" : "https://www.bootdev.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.bootdev.com">Click here</a>')


class TestParentNode(unittest.TestCase):
    def test_parent_no_tag(self):
        node = ParentNode(None, [], {})
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_parent_with_no_children(self):
        node = ParentNode("div", [], {})
        self.assertEqual(node.to_html(), "<div></div>")
        
    def test_parent_single_child(self):
        node = ParentNode("p", [LeafNode("b", "Bold text")], {})
        self.assertEqual(node.to_html(), "<p><b>Bold text</b></p>")
    
    def test_parent_node_with_multiple_children(self):
        node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "Italic text"),
        LeafNode(None, "Another normal text")
        ], {})
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Another normal text</p>")
   
    
    def test_parent_node_with_self_closing_tag(self):
        node = ParentNode("img", [], {"src": "image.jpg", "alt": "Image description"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="Image description"/>')

    def test_parent_node_with_mixed_content(self):
        node = ParentNode("div", [
            LeafNode("b", "Bold text"),
            "Normal text",
            LeafNode("i", "Italic text")
        ], {})
        self.assertEqual(node.to_html(), "<div><b>Bold text</b>Normal text<i>Italic text</i></div>")


if __name__ == "__main__":
    unittest.main()