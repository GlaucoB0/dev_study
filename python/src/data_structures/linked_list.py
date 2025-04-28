#
# Linked Lists são usadas quando queremos mais performace na adição e remoção de um elemento em uma lista
# Os itens são alocados em diferentes lugares na memoria, pois cada nó é ligado ao proximo por um atributo
#

class Node:
    def __init__(self, value): # __init__ é o construtor da classe
        self.data = value
        self.next = None # Ligando ao proximo nó

    def __str__(self): # __str__ é como eu quero que apareca toda vez q o print() for chamado
        return str(self.data)

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def pretend(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return self
        else:
            new_node.next = self.head
            self.head = new_node
            return self
    
    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return self
        else:
            self.tail.next = new_node
            self.tail = new_node
            return self

    def printer(self):
        node = self.head
        while node != None:
            print(f"[ {node} ]", end=" -> ")
            node = node.next

        

lista = List()

lista.pretend(3).pretend(2).pretend(1).append(4)

print(lista.printer())