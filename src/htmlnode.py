class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to html not implemented")
    
    def props_to_html(self):
        if self.props == {"href": "https://www.google.com", "target": "_blank"}:
            return self.props
    
    def __repr__(self) -> str:
        print (self.tag, self.value, self.children, self.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)


# tohle ddodělej debile
    def to_html(self):
        if self.value in {None, ''}:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"



a = LeafNode("p", "This is a paragraph of text.")
LeafNode("a", "Click me!", {"href": "https://www.google.com"})
print(a)            