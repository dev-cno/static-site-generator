

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
            return None
        
        result = ""
        for key, value in self.props.items():
            pair = f'{key}="{value}"'
            if result != "":
                result += " "
            result += pair
        return result
    
    def __repr__(self):
        props_str = self.props_to_html()
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {props_str})'