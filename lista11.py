lista_com_duplicatas = [1,2,3,1,4,2,5,6,3,7,8,5,9]

#inicializando uma lista vazia para armazenar os elemntos unicos
lista_sem_duplicatas = []

# Usando loop while para percorrer a lista e remover os elementos duplicados

while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) #pop é usada para remover o elemento
    if elemento not in lista_sem_duplicatas: #not in não esta presente
        lista_sem_duplicatas.append(elemento)
        
print('A lista sem duplicatas é:', lista_sem_duplicatas)