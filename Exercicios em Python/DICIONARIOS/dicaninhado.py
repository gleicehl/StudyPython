""" 
Dicionários podem armazenar qualquer tipo de objeto Python como valor
desde que a chave para esse valor seja um objeto imutável.
(strings e números)

"""
#Exemplo de DICIONÁRIO ANINHADO
Pessoas = {
    "pessoa1": {"nome": "Ana", "idade": 19},
    "pessoa2": {"nome": "Bruno", "idade": 23},
    "pessoa3": {"nome": "Danylo", "idade": 21},
    "pessoa4": {"nome": "Giovanni", "idade": 19, "contatos": {"1":"0000-0000", "2": "email@"}} 
    #A pessoa 4 possui um dict dentro
}
print("\n----------------------------------------")
print("     VAMOS ANALISAR A PESSOA1...")
print("----------------------------------------\n")
print("Imprimindo chave pessoa1: ", Pessoas["pessoa1"]) #imprimindo chaves da pessoa1
idade= Pessoas["pessoa1"]["idade"] #acessa chave idade da pessoa1 = 19
print("Imprimindo chave idade da pessoa1: ", idade) #imprime apenas a chave idade da pessoa1

print("\n----------------------------------------")
print("    AGORA VAMOS ANALISAR A PESSOA4...")
print("----------------------------------------\n")
#Imprimindo pessoa4
print("Imprimindo chave pessoa4: ",Pessoas["pessoa4"]) 

#Imprimindo a lista encadeada (contatos) existente na pessoa4
contatos= Pessoas["pessoa4"]["contatos"] #acessando dicionário contatos
print("Dicionário contatos completo: ", contatos) #Imprimindo todo o dicionário contatos
contatos= Pessoas["pessoa4"]["contatos"]["2"] #acessando chave do dicionário contatos
print("Chave 2 existente em contatos: ",contatos)

