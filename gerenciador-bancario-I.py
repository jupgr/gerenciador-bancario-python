def gerenciar_conta():
    saldo = 1000.00 
    transacoes = 0    

    while True:
        print("1")
        print("2")
        print("3")
        print("4")
        
        opcao = int(input())
        
        if opcao == 1:
            print(f"{saldo:.2f}")
        
        elif opcao == 2:
            valor_saque = float(input())
            if valor_saque <= saldo:
                saldo -= valor_saque
                transacoes += 1  
                print(f"{saldo:.2f}")
            else:
                print("Insuficiente")
        
        elif opcao == 3:
            valor_deposito = float(input())
            saldo += valor_deposito
            transacoes += 1  
            print(f"{saldo:.2f}")
        
        elif opcao == 4:
            print(f"{transacoes}")
            break
        
        else:
            print("Opção inválida")

gerenciar_conta()
