import os

usuarios = ()

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear') # fiz pra poder deixar bonitinho o terminal

def verifica_18(tupla):
    lista = []
    contador = 0 
    for e in tupla:
        if e['idade'] > 18:
            lista.append(e)
            contador += 1
    return {"qtd": contador, "list": lista}

clear()
while True:
    
    sair = input("\nSe deseja sair digite 'sair'\nPara adicionar um usuario aperte enter\n").lower()
    if sair == "sair":
        break

    clear()

    nome = input("Digite um nome: ")
    idade = input("Digite um idade: ")

    try:
        idade = int(idade)
    except:
        print("Valor de idade inválido.")
        continue
    
    usuarios = list(usuarios)
    usuarios.append({"nome": nome, "idade": idade})
    usuarios = tuple(usuarios)
clear()

lista18 = verifica_18(usuarios)
print(f"\nUsuarios: {usuarios}\nQuantos tem mais de 18 anos? : {lista18['qtd']}\nLista de pessoas maiores de 18: {lista18['list']}")


