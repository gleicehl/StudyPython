def criarUsuario():
    print("\nDigite seus dados abaixo para criar um perfil de cliente!")

    listaUsuarios = []

    while True:
        sair = int(input("\nDigite 1 para continuar ou 0 para sair: "))

        if sair == 0:
            print("\nSaindo da sessão!")
            break

        usuario = []
        nome = input("\nNome: ")
        dataNascimento = input("\nData de nascimento: ")
        logradouro = input("\nLogradouro: ")

        if dataNascimento.isdigit():
            print("Data de nascimento aceita!")
        else:
            print("\nDigite apenas números para a data de nascimento!")

        if dataNascimento.isdigit():
            usuario.append(nome)
            usuario.append(dataNascimento)
            usuario.append(compararCPF())
            usuario.append(logradouro)
            listaUsuarios.append(usuario)

    return listaUsuarios

def compararCPF():
    CPF = []

    while True:
        cpf1 = input("Digite seu CPF: ")

        if cpf1 in CPF:
            print("CPF já existe. Digite um novo CPF.")
        else:
            CPF.append(cpf1)
            return cpf1

def depositarSaldo(depositoTotal, extrato1):
    depositar = float(input("Digite um valor para depositar: "))
    if depositar > 0:
        depositoTotal = depositoTotal + depositar
        extrato1.append(f"Depósito total R$ {depositar:.2f}")
        return depositoTotal
    else:
        print("Valor inválido, digite um valor acima de 0 para depositar!")
        return depositoTotal

def sacarSaldo(saqueTotal, contSaques, depositoTotal, extrato1):
    sacar = float(input("Digite o valor do saque: "))
    if sacar <= 0:
        print("\nSaque inválido. O valor deve ser maior que 0!")
    elif contSaques >= 3:
        print("\nVocê atingiu o máximo de saques diários (3 por dia)!")
    elif saqueTotal > 1500:
        print("\nSaque inválido. Você atingiu o máximo de valor nos saques (R$1500,00)!")
    elif sacar > depositoTotal:
        print("\nSaldo insuficiente para sacar!")
    elif sacar > 500:
        print("\nSaque inválido. Só é possível sacar até R$500,00!")
    else:
        saqueTotal += sacar
        contSaques += 1
        restoSaque = depositoTotal - saqueTotal
        extrato1.append(f"Saque total R$ {sacar:.2f}")
        print("\nSaldo restante na conta: R$" + str(restoSaque))
    return saqueTotal, contSaques, restoSaque

def extratoConta(extrato1, restoSaque):
    for i in extrato1:
        print(i)
    print(f"Saldo atual: R${restoSaque:.2f}")

lista_de_usuarios = criarUsuario()
print("Lista de Usuários:")
for usuario in lista_de_usuarios:
    print(usuario)

menu = """
[0] Sair:
[1] Depositar:
[2] Sacar:
[3] Extrato:

"""
extrato1 = []
depositoTotal = 0
limiteDepositoPDia = 0
contSaques = 0
saqueTotal = 0
restoSaque = 0

while True:
    print("\nEscolha uma das opções a seguir:")
    opcao = int(input(menu))

    if opcao == 0:
        print("Obrigado pela preferência!")
        break

    if opcao == 1:
        depositoTotal = depositarSaldo(depositoTotal, extrato1)

    if opcao == 2:
        saqueTotal, contSaques, restoSaque = sacarSaldo(saqueTotal, contSaques, depositoTotal, extrato1)

    if opcao == 3:
        extratoConta(extrato1, restoSaque)
