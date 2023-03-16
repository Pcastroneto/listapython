numeros = [111,7,2,1] #lista normal
print(len(numeros)) # quantia de elementos
print(numeros) # lista sem alteração

###

numeros.append(4) #adcionamos o numero 4
print(len(numeros)) #contamos mais uma vez e vai dar 5 elementos por acrescentarmos mais o numero 4
print(numeros)

###

numeros.insert(0,222) # posição, valor
print (len(numeros)) # numero de elementos 6
print (numeros) # agora lista com o 222, na primeira posição, indicada pelo 0