#Conjuntos em python não suportam 
#indexação e nem fatiamento, caso queira
#acessar os seus valores é necessário 
#converter o conjunto para lista


numeros = {1, 2, 3, 4}
numeros = list(numeros)
print(numeros[0])