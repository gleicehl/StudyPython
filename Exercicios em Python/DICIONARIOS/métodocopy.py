Pessoas = {
    "pessoa1": {"nome": "Ana", "idade": 19},
    "pessoa2": {"nome": "Bruno", "idade": 23},
    "pessoa3": {"nome": "Danylo", "idade": 21},
    "pessoa4": {"nome": "Giovanni", "idade": 19, "contatos": {"1":"0000-0000", "2": "email@"}} 
    #A pessoa 4 possui um dict dentro
}

#cria uma cópia do dicionário existente
copia = Pessoas.copy()
copia["pessoa5"] = {"nome": "Gleice", "idade": "20"}
print(copia)
