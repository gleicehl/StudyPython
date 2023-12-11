#Exemplos de escrita do dicionário

pessoa = {"nome": "Gleice", "idade": 20}

pessoa = dict(nome= "Gleice", idade=20)

#adicionando uma chave nova no dicionário
pessoa ["telefone"]= "0000-0000"

#COMO ACESSAR VALORES DO DICIONÁRIO?
dados = {"nome":"Gleiceh", "idade":20}

#dados["nome"] -> forma de acessar o dado
#dados["nome"] = "Gleice" -> forma de modificar

print(dados)
print(dados["nome"])
dados["nome"] = "Gleice"
print(dados["nome"])



