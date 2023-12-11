#POP -> remove uma chave do dicionário

Pessoas = {
    "pessoa1": {"nome": "Ana", "idade": 19},
    "pessoa2": {"nome": "Bruno", "idade": 23},
    "pessoa3": {"nome": "Danylo", "idade": 21},
    "pessoa4": {"nome": "Giovanni", "idade": 19, "contatos": {"1":"0000-0000", "2": "email@"}} 
    #A pessoa 4 possui um dict dentro
}

print(Pessoas.pop("pessoa4", {}))
print (Pessoas)


print("\n---------------------------------\n")

#SETDEFAULT-> Adiciona uma chave que não existe
#Não adiciona se já existir uma mesma chave com valor já atribuido

Contato = {"nome": "Gleice", "numero": "0000-0000"}
Contato.setdefault("idade", "20")

print(Contato)

print("\n---------------------------------\n")

#UPDATE-> Atualiza uma chave existente ou adiciona uma chave não existente

Pessoas.update({"pessoa1": {"nome": "Aninha", "idade":19}})
Pessoas.update({"pessoa4": {"nome": "Giovanni", "idade":19}})
print(Pessoas)

print("\n---------------------------------\n")
#VALUES-> retorna todos os valores que estão nas chaves

print(Pessoas.values())

print("\n---------------------------------\n")
#IN -> Retorna se uma chave existe ou não

print("pessoa5" in Pessoas)
print("pessoa4" in Pessoas)

print("\n---------------------------------\n")
#DEL-> Remove uma chave 

del Pessoas["pessoa2"]
del Pessoas["pessoa1"]["idade"]
print(Pessoas)




