import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq_false(self):
        node1 = TextNode("test text", TextType.normal_type, "url")
        node2 = TextNode("you evil bro", TextType.bold_type, "url")
        self.assertNotEqual(node1, node2)

    def test_eq_false2(self):
        node3 = TextNode("different text", TextType.italic_type)
        node4 = TextNode("different text", TextType.code_type, "url")
        self.assertNotEqual(node3, node4)

    def test_eq(self):
        node1 = TextNode("different text", TextType.link_type, "url")
        node2 = TextNode("different text", TextType.link_type, "url")
        self.assertEqual(node1, node2)
        
    def test_eq_url(self):
        node6 = TextNode("different text", TextType.img_type, "url.exe")
        node7 = TextNode("different text", TextType.img_type, "url.exe")
        self.assertEqual(node6, node7)
    
    def test_repr(self):
        node7 = TextNode("you evil bro", TextType.bold_type, "url")
        self.assertEqual("TextNode(you evil bro, bold, url)", repr(node7))
    
        

if __name__ == "__main__":
    unittest.main()