
import unittest

from htmlnode import HTMLNode, LeafNode

dict_a = {
    "href": "https://www.google.com",
    "target": "_blank",
}
dict_b = {
    "src": "asset/project-architecture.png",
    "alt": "Image description",
}

node1 = HTMLNode("a","This is a piece of text", None, dict_a)
node2 = HTMLNode("a","This is a piece of text" ,None, dict_a)
node3 = HTMLNode("ismap","asset/project-architecture.png", [node1, node2], dict_b)
node4 = HTMLNode("ismap","asset/project-architecture.png", None, None)

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_node1(self):
        test_node = HTMLNode.props_to_html(node1)
        expected_output = 'href="https://www.google.com" target="_blank"'
        print("\nTesting test_props_to_html on node1...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {test_node}")
        self.assertEqual(test_node, expected_output)


    def test_props_to_html_node2(self):
        test_node = HTMLNode.props_to_html(node2)
        expected_output = 'href="https://www.google.com" target="_blank"'
        print("\nTesting test_props_to_html on node2...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {test_node}")
        self.assertEqual(test_node, expected_output)

    def test_props_to_html_node3(self):
        test_node = HTMLNode.props_to_html(node3)
        expected_output = 'src="asset/project-architecture.png" alt="Image description"'
        print("\nTesting test_props_to_html on node3...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {test_node}")
        self.assertEqual(test_node, expected_output)

    def test_props_to_html_node4(self):
        test_node = HTMLNode.props_to_html(node4)
        expected_output = ""
        print("\nTesting test_props_to_html on node4...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {test_node}")
        self.assertEqual(test_node, expected_output)


    def test_repr_node1(self):
        repr_node = repr(node1)
        props_str = str({'href': 'https://www.google.com', 'target': '_blank'})
        expected_output = f'HTMLNode(a, This is a piece of text, None, {props_str})'
        print("\nTesting __repr__ on node1...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {repr_node}")
        self.assertEqual(repr_node, expected_output)

    def test_repr_node2(self):
        repr_node = repr(node2)
        props_str = str({'href': 'https://www.google.com', 'target': '_blank'})
        expected_output = f'HTMLNode(a, This is a piece of text, None, {props_str})'
        print("\nTesting __repr__ on node2...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {repr_node}")
        self.assertEqual(repr_node, expected_output)

    def test_repr_node3(self):
        repr_node = repr(node3)
        props_str = str({'src': 'asset/project-architecture.png', 'alt': 'Image description'})
        expected_output = f"HTMLNode(ismap, asset/project-architecture.png, [{repr(node1)}, {repr(node2)}], {props_str})"
        print("\nTesting __repr__ on node3..")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {repr_node}")
        self.assertEqual(repr_node, expected_output)

    def test_repr_node4(self):
        repr_node = repr(node4)
        expected_output = 'HTMLNode(ismap, asset/project-architecture.png, None, None)'
        print("\nTesting __repr__ on node4...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {repr_node}")
        self.assertEqual(repr_node, expected_output)




class TestLeafNode(unittest.TestCase):
    dict_a = {"href": "https://www.google.com"}
    child_node1 = LeafNode("p", "Hello, world!")
    child_node2 = LeafNode("a", "Click me!", dict_a)
    child_node3 = LeafNode("p", "Testing...")

    def test_leaf_to_html_1(self):
        test_node = self.child_node1.to_html()
        expected_output = "<p>Hello, world!</p>"
        print("\nTesting to_html() on child_node1...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {test_node}")
        self.assertEqual(test_node, expected_output)

    def test_leaf_to_html_2(self):
        test_node = self.child_node2.to_html()
        expected_output = '<a href="https://www.google.com">Click me!</a>'
        print("\nTesting to_html() on child_node2...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {test_node}")
        self.assertEqual(test_node, expected_output)

    def test_leaf_to_html_3(self):
        test_node = self.child_node3.to_html()
        expected_output = "<p>Testing...</p>"
        print("\nTesting to_html() on child_node3...")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {test_node}")
        self.assertEqual(test_node, expected_output)

if __name__ == "__main__":
    unittest.main()



