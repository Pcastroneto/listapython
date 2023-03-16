lista = [17,8,10,6,2,4] #lista para ordenar
trocado = True # precisamos dele para entrar no loop while

while trocado:
    trocado = False # sem trocas até agora
    for i in range(len(lista) -1):
        if lista[i] > lista[i + 1]:
            trocado = True # ocorreu uma troca 
            lista[i], lista[i+1] =lista[i+1], lista[i]
print(lista)