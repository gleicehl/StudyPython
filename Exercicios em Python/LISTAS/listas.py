# FORMAS DIFERENTES DE ESCREVER UMA LISTA:

frutas = ["laranja", "uva", "morango"]

frutas2 = []
# basta fazer input e adicionar variaveis

letras= list("python")
numeros= list(range(10))
pessoa= ["Gleice", "estudante", 20, 143790, True]

print("---------------------------------------")
print(frutas)
print(frutas2)
print(letras)
print(numeros)
print(pessoa)

print("---------------------------------------")
# IMPRIMINDO POSIÇÕES DE PESSOA[]:

print(pessoa[0])
print(pessoa[-1])

print("---------------------------------------")
# IMPRIMINDO POSIÇÕES DE PESSOA[] COM FOR:

for indice, dados in enumerate(pessoa):
    print(f"{indice}: {dados}")

print("---------------------------------------")
# OUTRA FORMA:

for dados in pessoa:
    print(dados)

print("---------------------------------------")
# IMPRIMINDO POSIÇÕES DE LETRAS[]:
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

print("---------------------------------------")
# COMO ACESSAR ALGO DA LISTA?

x=int(input("digite a quantidade de itens na lista: "))
i=0
# criando a lista aqui
nomes=[]
print("digite os nomes: ")
for i in range(x):
    nome= input("")
    nomes.append(nome)

y=int(input("Qual posição deseja acessar na lista: "))
# para imprimir é só colocar a posição em colchete
print(nomes[y])







