class Node():
    def __init__(self, value):
        self.data = value
        self.next = None
        
    def __str__(self):
        return str(self.data)

class Stack():
    def __init__(self):
        self.top = None

    def __str__(self):
        return str(self.top)
    
    def add(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        return new_node
    
    def remove(self):
        if self.is_empty():
            return None
        
        self.top = self.top.next

        return self
    
    def is_empty(self):
        return self.top == None
    
    
historico = Stack()

historico.add(1)
historico.add(2)

print(historico)