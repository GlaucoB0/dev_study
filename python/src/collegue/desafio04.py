usuarios = ()

while True:
    sair = input("\nSe deseja sair digite 'sair'\nPara adicionar outro usuario aperte enter\n").lower()
    if sair == "sair":
        break

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

def verifica_18(tupla):
    lista = []
    y = 0
    for e in tupla:
        if e['idade'] > 18:
            lista.append(e)
            y += 1
    return {"qtd_maior_18":y,"maiores_18_anos": lista}
            

print(f"\nUsuarios: {usuarios}\n,Maiores de 18 anos:{verifica_18(usuarios)}")


