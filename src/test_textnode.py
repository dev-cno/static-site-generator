import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()