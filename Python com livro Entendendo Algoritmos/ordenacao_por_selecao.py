#ordenar um array do menor para o maior

def encontrarMenor(array):
    menor_valor = array[0]
    menor_indice = 0  #representa o indice do menor valor encontrado até agora
    
    for item in range(1, len(array)): #iterar sobre o array, começando do indice 1 até o final
        if array[item] < menor_valor:
            menor_valor = array[item]
            menor_indice = item
    return menor_indice

def ordenacaoporSelecao(array):
    novo_array =[]
    for item in range(len(array)):
        menor_valor = encontrarMenor(array)
        novo_array.append(array.pop(menor_valor))
    return novo_array


print(ordenacaoporSelecao([5,8,2,7,1,9,11,14,75,4]))