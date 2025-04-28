# Retorna o index de um numero em uma lista crescente
def find_in(array, num):
    left = 0
    right = len(array) - 1
    i = 0
    while left <= right:
        mid = (left + right) // 2
        if num == array[mid]:
            return mid + i
        elif num > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1