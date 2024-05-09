import unittest

from htmlnode import HTMLnode

class TestHTMLnode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLnode({"href": "https://www.google.com", "target": "_blank"})
        node1 = HTMLnode({"href": "https://www.microsoft.com", "target": "_blank"})
