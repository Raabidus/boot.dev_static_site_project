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
        print (HTMLNode(self.value, self.children, self.props))

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children, props):
        super().__init__(value)


# tohle ddodělej debile
    def to_html(self):
        if self.LeafNode == "":
            raise ValueError
        else:
            return str(self.LeafNode)
        if self.tag == "":
            self.value == ""