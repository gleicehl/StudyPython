#Podemos combinar prâmetros obrigatórios com args e kwargs. 
#São definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente

def exibir_poema(data_extenso, *args, **kwargs):

    #"\n".join(args) está usando o método join da string para criar uma única string a partir dos elementos em args. 
    #O separador entre os elementos é a quebra de linha ("\n").
    texto = "\n".join(args)

    #uso do "\n".join para separar cada meta_dado por linha
    #cria-se um dicionário com o kwargs.items(), onde cada chave possui um valor
    #Cria-se a string: "{chave.title()}: {valor}" 
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("sexta-feira, 26 de agosto de 2022", "zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

