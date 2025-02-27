from textnode import *

def main():
    node1 = TextNode("test text", TextType.normal_type, "url")
    node2 = TextNode("test text", TextType.bold_type, "url")
    node3 = TextNode("different text", TextType.italic_type, "url")
    node4 = TextNode("different text", TextType.code_type, "url")
    node5 = TextNode("different text", TextType.link_type, "url")
    node6 = TextNode("different text", TextType.img_type, "url")
    
    print(f"Should be False: {node1 == node2}")
    print(f"Should be False: {node1 == node3}")
    print(node1)
    print(node2)
    print(node3)
    print(node4)
    print(node5)
    print(node6)

if __name__ == "__main__":
    main()