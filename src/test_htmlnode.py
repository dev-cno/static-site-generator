
import unittest

from htmlnode import HTMLNode

dict_a = {
    "href": "https://www.google.com",
    "target": "_blank",
}
dict_b = {
    "src": "asset/project-architecture.png",
    "alt": "Image description",
}

node1 = HTMLNode("a", "This is a piece of text", None, dict_a)
node2 = HTMLNode("a", "This is a piece of text" ,None, dict_a)
node3 = HTMLNode("ismap", "asset/project-architecture.png", [node1, node2], dict_b)
node4 = HTMLNode("ismap", "asset/project-architecture.png", None, None)



class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_node1(self):
        test_node = HTMLNode.props_to_html(node1)
        expected_output = 'href="https://www.google.com" target="_blank"'
        print("Testing test_props_to_html on node1...")
        self.assertEqual(test_node, expected_output)

    def test_props_to_html_node2(self):
        test_node = HTMLNode.props_to_html(node2)
        expected_output = 'href="https://www.google.com" target="_blank"'
        print("Testing test_props_to_html on node2...")
        self.assertEqual(test_node, expected_output)

    def test_props_to_html_node3(self):
        test_node = HTMLNode.props_to_html(node3)
        expected_output = 'src="asset/project-architecture.png" alt="Image description"'
        print("Testing test_props_to_html on node3...")
        self.assertEqual(test_node, expected_output)

    def test_props_to_html_node4(self):
        test_node = HTMLNode.props_to_html(node4)
        expected_output = None
        print("Testing test_props_to_html on node4...")
        self.assertEqual(test_node, expected_output)


    def test_repr_node1(self):
        repr_node1 = repr(node1)
        expected_output_node1 = 'HTMLNode(a, This is a piece of text, None, href="https://www.google.com" target="_blank")'
        print("Testing __repr__ on node1...")
        self.assertEqual(repr_node1, expected_output_node1)

    def test_repr_node2(self):
        repr_node2 = repr(node2)
        expected_output_node2 = 'HTMLNode(a, This is a piece of text, None, href="https://www.google.com" target="_blank")'
        print("Testing __repr__ on node1...")
        self.assertEqual(repr_node2, expected_output_node2)

    def test_repr_node3(self):
        repr_node3 = repr(node3)
        expected_output_node3 = f'HTMLNode(ismap, asset/project-architecture.png, [{repr(node1)}, {repr(node2)}], src="asset/project-architecture.png" alt="Image description")'
        print("Testing __repr__ on node1...")
        self.assertEqual(repr_node3, expected_output_node3)

    def test_repr_node4(self):
        repr_node4 = repr(node4)
        expected_output_node4 = 'HTMLNode(ismap, asset/project-architecture.png, None, None)'
        print("Testing __repr__ on node1...")
        self.assertEqual(repr_node4, expected_output_node4)


if __name__ == "__main__":
    unittest.main()



