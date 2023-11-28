
letras=["a", "elie", "o", "ulala"]
letras.sort()
print(letras)

# para inverter a lista:
letras=["a", "elie", "o", "ulala"]
letras.sort(reverse=True)
print(letras)

# Para colocar em ordem crescente
# O len conta variaveis da lista
letras=["a", "elie", "o", "ulala"]
letras.sort(key=lambda x: len(x))
print(letras)

# Para colocar em ordem decrescente
letras=["a", "elie", "o", "ulala"]
letras.sort(key=lambda x: len(x), reverse=True)
print(letras)