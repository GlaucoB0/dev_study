class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
         self.first = None
         self.final = None

    def __str__(self):
        if self.first == None:
            return "None"
        
        content = "Inicio → "
        current = self.first
        while current is not None:
            content += f"[ {current.value} ] ← "
            current = current.next

        return content + "Final"
    
    def add(self, value):
        new_node = Node(value)

        if self.first == None:
            self.first = new_node
            self.final = new_node
        else:
            self.final.next = new_node
            self.final = new_node
        
        return self
    
    def remove(self):
        if self.first == None:
            return None
        else:
            self.first = self.first.next
            return self

    

fila = Queue()

fila.add(1)
fila.add(5)
fila.add(4)

print(fila)