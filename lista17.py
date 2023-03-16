#etapa 1
banda = []
print('etapa 1:', banda)
#Etapa 2:
banda.append('John lennon')
banda.append('paul McCartney')
banda.append('George harrison')
print('etapa 2:', banda)
#Etapa 3:
for membros in range(2):
    banda.append(input('Novo membro: '))
print('etapa3:', banda)
#Etapa 4:
del banda[-1]
del banda[-1]
print('etapa 4:', banda)
#etapa 5:
banda.insert(0,'RingoStarr')
print('etapa 5:',banda)
print('The fab',len(banda))