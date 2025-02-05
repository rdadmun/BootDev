from tests.textnode import TextNode, TextType

def main():
    node = TextNode("Example text", TextType.BOLD)
    print(node)
    
if __name__ == "__main__":
    main()