#Criando lista
lista= [1,2,3,4,5]
#Usando um loop for para percorrer a lista e imprimir cada elemento
for i in range(len(lista)): # Ou seja ele foi até o range da list aque é até de 0 até , só sabemos isso por causa do len  dizendo que tem 5 elementos
    print('o elemento', i+1,'da lista é:', lista[i])
    
 #Criando uma lista de numeros
numeros =[1,9,3,4,10]
#Usando loop for para percorrer a lista e imprimir cada elemento
for numero in numeros:  #numero é o valido do resultado dos numeros
    print(numero, "-com for")
    
#Usando loop while para percorrer a lista e imprimir cada elemento
i = 0
while i < len(numeros):
    print(numeros[i], '- Com While')
    i += 1 # Aqui ele vai incrementando mais