# Ordena uma lista em ordem crescente
def sort_cres(array):
    y = 0
    while y < len(array)-1:
        i=0
        while i < len(array)-1:
            if array[i] > array[i+1]:
                g = array[i+1]
                array[i+1] = array[i]
                array[i] = g
            i+=1
        y+=1
    return array

# Ordena uma lista em ordem decrescente
def sort_dec(array):
    y = 0
    while y < len(array)-1:
        i=0
        while i < len(array)-1:
            if array[i] < array[i+1]:
                g = array[i+1]
                array[i+1] = array[i]
                array[i] = g
            i+=1
        y+=1
    return array