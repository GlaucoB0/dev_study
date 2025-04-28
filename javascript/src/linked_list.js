class Node {
    constructor(value){
        this.value = value
        this.next = null
    }
}

class List {
    constructor(){
        this.head = null
        this.tail = null
    }

    prepend(value){ // Adiciona um nó no inicio da lista
        let newNode = new Node(value) 

        if (this.head == null){
            this.head = newNode
            this.tail = newNode
        } else {
            newNode.next = this.head
            this.head = newNode
        }
        return this
    }

    append(value){// Adiciona um nó no final da lista
        let newNode = new Node(value)
        if (this.tail == null){
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            this.tail = newNode
        }
        return this
    }

    find(value){ // Procura um valor dentro da lista
        let current = this.head
        while(current.next !== null){
            if(current.value == value){
                return current
            }
            current = current.next
        }
        if(current.value == value){
            return current
        }
        return undefined
    }

    delete(value){ // Deleta um valor da lista
        if(!this.head) return undefined

        if(this.head.value == value){
            this.head = this.head.next
            if(!this.head){
                this.tail = null
            }
            return this
        }

        let current = this.head
        while(current.next !== null){
            if(current.next.value == value){
                if(this.tail == current.next){
                    this.tail = current
                }
                current.next = current.next.next
                return this
            }
            current = current.next
        }
        return undefined
    }

}

const list = new List()

list.prepend(5)
list.append(3).append(6).append(2).append(1)

console.log(list.find(1))