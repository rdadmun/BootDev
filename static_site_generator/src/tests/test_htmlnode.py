import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="tag", value="parent", props={"class": "container", "id": "kernel"})
        method_output = node.props_to_html()
        self.assertEqual(method_output, ' class="container" id="kernel"')
    

    def test_values(self):
        node = HTMLNode("tag", "parent")
        
        self.assertEqual(node.tag, "tag")
        self.assertEqual(node.value, "parent")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("tag", "parent", None, props={"class": "container", "id": "kernel"})
        node_2 = HTMLNode("tag", "parent", ['child_1', 'child_2'], None)
        
        self.assertEqual(repr(node), "HTMLNode(tag, parent, children: None, {'class': 'container', 'id': 'kernel'})")
        self.assertEqual(repr(node_2), "HTMLNode(tag, parent, children: ['child_1', 'child_2'], None)")

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_value_none(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_tag_none(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

class TestParentNode(unittest.TestCase):

    def test_example(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()