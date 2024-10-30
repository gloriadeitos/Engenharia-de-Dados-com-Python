# Nome: Glória Maria Deitos Gomes da Silva
# Data: 30/Outubro/2024

# Dados globais
usuarios = []
contas = []
numero_conta = 1
AGENCIA = "0001"

# Função para saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

# Função para depósito
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função para cadastrar usuário
def criar_usuario(nome, nascimento, cpf, endereco):
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado com esse CPF!")
        return None
    usuario = {"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    return usuario

# Função para criar conta corrente
def criar_conta_corrente(cpf):
    global numero_conta
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return None
    conta = {"agencia": AGENCIA, "numero": numero_conta, "usuario": usuario}
    contas.append(conta)
    numero_conta += 1
    print("Conta criada com sucesso!")
    return conta

# Menu principal
def menu_bancario():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[u] Novo Usuário\n[c] Nova Conta\n[q] Sair\n=> ")

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite, 
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            nome = input("Nome: ")
            nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            criar_usuario(nome, nascimento, cpf, endereco)

        elif opcao == "c":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta_corrente(cpf)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executar o menu bancário
menu_bancario()
