# MAIÚSCULO - MINÚSCULO - TITLE:

Palavra = "Gleice"

print(Palavra.upper())
print(Palavra.lower())
print(Palavra.title())

# ELIMINANDO ESPAÇOS EM BRANCO:
# TODO ESPAÇO - ESQUERDA - DIREITA 

print("--------------------------")

Palavra2= "   Gleice  "

print("\n" + Palavra2.strip())
print(Palavra2.lstrip())
print(Palavra2.rstrip())

#JUNÇÃO E CENTRALIZAÇÃO

print("--------------------------")

Palavra3= "Gleice"
nome = ("Heloise")

print("\n"+Palavra3.center(10, "H"))
print("-".join(Palavra3))

print("--------------------------")

# JUNTANDO DUAS STRINGS ENTRELAÇADAS

string1 = "Gleice"
string2 = "Heloise"
resultado = ""

tamanho_menor = min(len(string1), len(string2))

for i in range(tamanho_menor):
    resultado += string1[i] + string2[i]

# Adicionar o restante da string mais longa, se houver
if len(string1) > len(string2):
    resultado += string1[tamanho_menor:]
else:
    resultado += string2[tamanho_menor:]

print(resultado)

# IMPRIMINDO VARIÁVEIS
print("--------------------------")

nome="Gleice"
idade=20
profissao="programadora"

print("Oi, meu nome é %s, tenho %d, e sou uma %s" %(nome, idade, profissao))
print(f"Oi, meu nome é {nome}, tenho {idade}, e sou uma {profissao}")


# FORMATANDO VARIÁVEIS

print("--------------------------")

PI=3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

# FATIAMENTO

print("--------------------------")

Nomecompleto= "Gleice Heloise"

print(Nomecompleto[0])
print(Nomecompleto[:6])
print(Nomecompleto[7:])
print(Nomecompleto[:])
print(Nomecompleto[0:3])
print(Nomecompleto[0:6:2])
print(Nomecompleto[::-1])

# STRINGS MULTIPLAS LINHAS 
print("--------------------------")

nome2="Gleice"

mensagem= f'''
Olá meu nome é {nome2}, 
estou aprendendo python'''

print(mensagem)


