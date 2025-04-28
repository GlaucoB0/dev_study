# Conta quantas vogais tem uma string
def count_vowels(word: str) -> int:
    word = word.lower()
    vog = 0
    for l in word:
        if l in {"a", "e", "i", "o", "u"}:
            vog +=1
    return vog

# Inverte uma palavra
def reverse_string(word: str) -> str:
    reversed_word = []

    for i in range(len(word)-1, -1, -1): # Começa no tamanho-1 e termina do -1 diminuindo 1--
        reversed_word.append(word[i])

    return "".join(reversed_word)