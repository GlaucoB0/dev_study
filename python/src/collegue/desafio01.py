frase = input("Digite uma frase: ")

tres_palavras = frase.split()[:3]

for i, e in enumerate(tres_palavras):
    print(f"index: {i}, word: {e}")

inverso = tres_palavras[::-1]

print("frase inversa: ", inverso)