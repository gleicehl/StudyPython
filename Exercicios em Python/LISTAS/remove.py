# Revome o elemento da lista

numeros=[1,2,3]

numeros.remove(1)
print(numeros)

# No caso de haver repetição:

numeros2=[1,1,4,1]

rep=numeros2.count(1)

for i in range(rep):
    numeros2.remove(1)

print (numeros2)


