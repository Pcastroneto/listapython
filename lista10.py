numeros=[10,20,30,40,50]

#inicializando a variavel que ira aamarzenar o maior numero 
maior_numero = numeros[0]

# usando um loop for para percorrer a lista e econtrar o maior numero
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
        
print('O maior número na lista é:', maior_numero)