#Funçãoes também podem ser chamadas usando arqumentos nomeados, chave=valor

def carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}")

#nesse exemplo de chamada, todos os valores têm que está na ordem:
carro("fiat","palio","1999", "abc-1234")

#nesse exemplo de chamada, todos as chaves têm que ter o mesmo nome da chave dita na função: (modelo, marca, etc)
carro(marca="fiat",modelo="palio",ano="1999", placa="abc-1234")

#nesse exemplo de chamada, cria-se um dicionário:
carro(**{"marca":"fiat","modelo":"palio","ano":"1999", "placa":"abc-1234"})