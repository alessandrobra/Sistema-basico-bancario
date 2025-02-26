def depositar(conta):
    valor = float(input("Valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido!")
    return conta

def sacar(conta):
    valor = float(input("Valor do saque: "))
    if valor > conta["saldo"]:
        print("Saldo insuficiente!")
    elif valor > 500:  # limite por operação
        print("Excede o limite de saque!")
    elif conta["numero_saques"] >= 3:
        print("Número máximo de saques atingido!")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
    else:
        print("Valor inválido!")
    return conta

def exibir_extrato(conta):
    print("\n======= EXTRATO =======")
    print(conta["extrato"] if conta["extrato"] else "Sem movimentações.")
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("=======================")

def buscar_usuario(usuarios, cpf):
    # Filtra a lista de usuários para encontrar o usuário com o CPF informado
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if buscar_usuario(usuarios, cpf) is not None:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço: ")
    usuario = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")

def criar_conta_corrente(usuarios, contas, agencia):
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    usuario = buscar_usuario(usuarios, cpf)
    if usuario:
        numero_conta = len(contas) + 1  # numeração sequencial
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": "",
            "numero_saques": 0
        }
        contas.append(conta)
        print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Crie o usuário primeiro.")

def selecionar_conta(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    print("\nContas disponíveis:")
    for conta in contas:
        print(f"Conta: {conta['numero_conta']} - Titular: {conta['usuario']['nome']}")
    try:
        numero = int(input("Digite o número da conta: "))
    except ValueError:
        print("Número inválido!")
        return None
    for conta in contas:
        if conta["numero_conta"] == numero:
            return conta
    print("Conta não encontrada!")
    return None

def main():
    menu = """
===== MENU =====
[1] Criar Usuário
[2] Criar Conta Corrente
[3] Listar Contas
[4] Depositar
[5] Sacar
[6] Extrato
[7] Buscar Usuário por CPF
[8] Sair
=> """
    usuarios = []
    contas = []
    agencia = "0001"

    while True:
        opcao = input(menu)

        if opcao == "1":
            criar_usuario(usuarios)

        elif opcao == "2":
            criar_conta_corrente(usuarios, contas, agencia)

        elif opcao == "3":
            if contas:
                print("\nContas cadastradas:")
                for conta in contas:
                    print(f"Conta: {conta['numero_conta']} - Titular: {conta['usuario']['nome']}")
            else:
                print("Nenhuma conta cadastrada.")

        elif opcao == "4":
            conta = selecionar_conta(contas)
            if conta is not None:
                depositar(conta)

        elif opcao == "5":
            conta = selecionar_conta(contas)
            if conta is not None:
                sacar(conta)

        elif opcao == "6":
            conta = selecionar_conta(contas)
            if conta is not None:
                exibir_extrato(conta)

        elif opcao == "7":
            cpf = input("Digite o CPF para busca: ")
            usuario = buscar_usuario(usuarios, cpf)
            if usuario:
                print(f"Usuário encontrado: {usuario['nome']} - CPF: {usuario['cpf']}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "8":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

if __name__ == '__main__':
    main()
