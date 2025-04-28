# Somar todos os numeros pares de 0 até n
def sum_even_numbers(n: int) -> int:
    sum = 0
    for i in range(0, n + 1, 2):
        sum += i
    return sum

# Fatorial
def factorial(num: int) -> int:
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac

# Verifica se um numero passado é primo ou não
def is_primeNumber(num):
    i = 1
    div = 0
    while i<=num+1:
        if num % i == 0:
            div += 1
        i+=1
    if div == 2:
        return True
    else: 
        return False