# Maior sequencia crescente
def longest_increasing_subsequence(array: list) -> int:

    subsequence_length = 1
    max_length = 1

    for i in range(0, len(array)-1):
        if array[i] < array[i+1]:
            subsequence_length +=1
        else:
            max_length = subsequence_length
            subsequence_length = 1

    return max(max_length, subsequence_length)

# Retorna a quantidade de digitos da sequencia de fibonacci
def fibonacci(qtd):
    array = []
    a = 0
    b = 1
    i = 0
    while i<qtd:
        array.append(a)
        c = a+b
        a = b
        b = c
        i+=1
    return array