#COMO ITERAR DICIONÁRIOS USANDO FOR
Pessoas = {
    "pessoa1": {"nome": "Ana", "idade": 19},
    "pessoa2": {"nome": "Bruno", "idade": 23},
    "pessoa3": {"nome": "Danylo", "idade": 21},
    "pessoa4": {"nome": "Giovanni", "idade": 19, "contatos": {"1":"0000-0000", "2": "email@"}} 
    #A pessoa 4 possui um dict dentro
}

#ambas as formas tem resultados iguais, porém é melhor a 2º
for pessoa in Pessoas:
    print(pessoa, Pessoas[pessoa])
print("\n----------------------------------\n")
#essa segunda forma me retorna tuplas
for pessoa, valor in Pessoas.items():
    print(pessoa, valor)