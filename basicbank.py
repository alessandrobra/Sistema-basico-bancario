menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo, limite, extrato, numero_saques, LIMITE_SAQUES = 0, 500, "", 0, 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            saldo, extrato = saldo + valor, extrato + f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")
    
    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print("Excede o limite de saque!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques atingido!")
        elif valor > 0:
            saldo, extrato, numero_saques = saldo - valor, extrato + f"Saque: R$ {valor:.2f}\n", numero_saques + 1
        else:
            print("Valor inválido!")
    
    elif opcao == "3":
        print(f"\n======= EXTRATO =======\n{extrato if extrato else 'Sem movimentações.'}\nSaldo: R$ {saldo:.2f}\n======================")
    
    elif opcao == "4":
        break
    
    else:
        print("Opção inválida!")