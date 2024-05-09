import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is not a text node", None, "italic")
        self.assertEqual(node, node2, node3)


if __name__ == "__main__":
    unittest.main()
