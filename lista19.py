lista =[]
trocado = True
num = int(input('Quantos elemntos deseja? '))

for i in range(num):
    val = float(input('Entre com número: '))
    lista.append(val)
while trocado:
    trocado = False
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            trocado = True
            lista[i], lista[i+1] = lista[i+1], lista[i]
    
print('\nordenado:')
print(lista)
    