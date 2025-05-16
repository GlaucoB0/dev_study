valor = input("Digite um valor: ")

def getId(value):
    try:
        value = float(value)
        if value < 0:
            return None
        else:
            return id(value)
    except:
        print("Digite um valor valido!")

print(getId(valor))