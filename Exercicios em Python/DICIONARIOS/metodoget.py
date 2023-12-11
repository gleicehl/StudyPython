Pessoas = {
    "pessoa1": {"nome": "Ana", "idade": 19},
    "pessoa2": {"nome": "Bruno", "idade": 23},
    "pessoa3": {"nome": "Danylo", "idade": 21},
    "pessoa4": {"nome": "Giovanni", "idade": 19, "contatos": {"1":"0000-0000", "2": "email@"}} 
    #A pessoa 4 possui um dict dentro
}
#esse método retorna uma chave existente ou não

print(Pessoas.get("chave")) 
print(Pessoas.get("chave", {})) #se a chave não existir ele retorna: {}
print(Pessoas.get("pessoa1", {})) 
