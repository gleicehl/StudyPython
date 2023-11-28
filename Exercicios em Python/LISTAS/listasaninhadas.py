# LISTAS ANINHADAS SÃO MATRIZES DO PYTHON

x=[]
i=0
print("quem está em x? ")
for i in range(2):
    x1=int(input(""))
    x.append(x1)


print("\n quem está em y? ")
y=[]
for i in range(2):
    y1=int(input(""))
    y.append(y1)

matriz=[]
matriz.append(x)
matriz.append(y)
print(matriz)

print(matriz[0][0])
print(matriz[0][-1])


