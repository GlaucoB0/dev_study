class Stack {
    constructor() {
        this.items = []
    }

    push(value) { 
        return this.items.push(value) // Adiciona item ao topo
    }

    pop() { 
        if(this.items.length === 0){
            return undefined
        }
        return this.items.pop() // Remove o item do topo da lista
    }

    top() { 
        return this.items[this.items.length-1] // Verifica o topo da lista
    }

    size() {
        return this.items.length
    }
}

const pilha = new Stack()

pilha.push(5)
pilha.push(2)
pilha.push(2)
pilha.push(21)
pilha.push(22)
pilha.push(1)

console.log(pilha.top())