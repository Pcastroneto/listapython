lista = [10,1,8,3,5]

lista[0],lista[4] = lista[4],lista[0] # trocou o 0 por 4 mudando o elemento 0 para o elemento 4 (ou seja 10 pelo 5)
lista[1],lista[3] = lista[3],lista[1] # mesma coisa nesse mas com o 3 e 1 mudando o 1 e o 3

print(lista)