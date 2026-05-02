import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)


    def test_eq_2(self):
        node3 = TextNode("This is another text node", TextType.ITALIC)
        node4 = TextNode("This is another text node", TextType.CODE)
        self.assertNotEqual(node3, node4)

    def test_eq_3(self):
        node5 = TextNode("This is another text node", TextType.ITALIC, "https://google.com")
        node6 = TextNode("This is another text node", TextType.CODE)
        self.assertNotEqual(node5, node6)

    def test_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        expected_output = 'This is a text node'
        print("\nTesting text_node_to_html_node() on html_node1..")
        print(f"Expected result: {expected_output}")
        print(f"Actual:          {html_node}")
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, expected_output)

if __name__ == "__main__":
    unittest.main()