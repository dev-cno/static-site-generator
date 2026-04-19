

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("HTMLNode class method 'to_html' not yet implemented.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for key, value in self.props.items():
            if result != "":
                result += " "
            result += f'{key}="{value}"'
        return f'{result}'
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        if props_str:
            props_str = f" {props_str}"
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.props})'