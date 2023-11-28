lista=[1,2,3]

copia= lista.copy()

print(lista)
print(copia)

# Para mostrar que são diferentes:

print(id(lista), id(copia))

# também é possivel alterar a copia

for numero in range(len(copia)):
    copia[numero]=copia[numero]*2

print(copia)
print(lista)
