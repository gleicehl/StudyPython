class Banco:
    def __init__(self):
        # Dicionário para armazenar as contas dos clientes
        self.contas = {}

    def criar_conta(self, numero_conta, nome, saldo_inicial=0):
        # Verifica se a conta já existe
        if numero_conta in self.contas:
            print("Conta já existe.")
        else:
            # Cria uma nova conta com saldo inicial
            self.contas[numero_conta] = {
                "nome": nome,
                "saldo": saldo_inicial
            }
            print("Conta criada com sucesso.")

    def deposito(self, numero_conta, valor):
        # Verifica se a conta existe
        if numero_conta in self.contas:
            self.contas[numero_conta]["saldo"] += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Conta não encontrada.")

    def saque(self, numero_conta, valor):
        # Verifica se a conta existe
        if numero_conta in self.contas:
            # Verifica se há saldo suficiente para o saque
            if self.contas[numero_conta]["saldo"] >= valor:
                self.contas[numero_conta]["saldo"] -= valor
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta não encontrada.")

    def extrato(self, numero_conta):
        # Verifica se a conta existe
        if numero_conta in self.contas:
            print(f"Nome: {self.contas[numero_conta]['nome']}")
            print(f"Saldo: {self.contas[numero_conta]['saldo']}")
        else:
            print("Conta não encontrada.")


# Exemplo de uso do sistema bancário
banco = Banco()

# Criar contas
banco.criar_conta("12345", "João", 1000)
banco.criar_conta("67890", "Maria", 500)

# Realizar operações
banco.deposito("12345", 500)
banco.saque("67890", 200)

# Ver extratos
banco.extrato("12345")
banco.extrato("67890")
