class HTMLnode:
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
        print (HTMLnode(self.value, self.children, self.props))