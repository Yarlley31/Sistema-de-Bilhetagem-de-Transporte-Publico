# menu inicial
print("Bem-vindo ao Sistema de Bilhetagem de Transporte Público")
valor_passagem = float(input("insira o valor da passagem: "))
print("-" * 30, "\n")

# declaração de variáveis
continuar = 1
funcionalidade = 0
saldo = 0
valor_a_pagar = 0

while continuar == 1:
    categoria_passageiro = int(input("Selecione uma das categorias de passageiro:\n[1] padrão \n[2] estudante/idoso\n[3] social \n[4] Sair do sistema\n"))
    print("-" * 30, "\n")
    
    # categoria padrão
    if categoria_passageiro == 1:
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n"))
        print("-" * 30, "\n")
        
        # faz a recarga
        if funcionalidade == 1:
            recarga_total = 0
            recarga_total += 1
            
            recarga = float(input("Digite o valor da recarga: R$"))
            saldo = recarga
            recarga_valor_total_1 = 0
            recarga_valor_total_1 += recarga
            print("Recarga efetuada com sucesso")
            
        # faz a compra de passagens
        elif funcionalidade == 2:
            qnt_passagem_1 = int(input("Quantas passagens você quer comprar: "))
            valor_passagem *= qnt_passagem_1
            valor_total_passagem_1 = valor_passagem
            if saldo >= valor_passagem:
                print("Compra efetuada com sucesso!")
            else:
                print("Compra mal sucedida, devido a falta de saldo")
                
        # mostra o saldo
        elif funcionalidade == 3:
            if saldo >= recarga:
                print(f"Você tem saldo suficiente para embarcar!")
            else:
                print("Você não tem saldo suficiente!")
        
        # sai do while
        elif funcionalidade == 4:
            print("Até a próxima")
            continuar = 0
        
    # categoria estudante/idoso
    elif categoria_passageiro == 2:
        
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo \n[4] Sair do sistema\n"))
        
        # faz a recarga
        if funcionalidade == 1:
            recarga = float(input("Digite o valor da recarga: R$"))
            saldo = recarga
            print("Recarga efetuada com sucesso!")
        
        # faz a compra de passagens
        elif funcionalidade == 2:
            qnt_passagem = int(input("Quantas passagens você quer comprar: "))
            valor_passagem = (valor_passagem / 2) * qnt_passagem 
            if saldo >= valor_passagem:
                print(f"Compra efetuada com sucesso!\nValor = R${valor_passagem:.2f}")
                saldo -= valor_passagem
            else:
                print("Compra mal sucedida, devido a falta de saldo")
        
        # mostra o saldo
        elif funcionalidade == 3:
            print(f"Você tem R${saldo:.2f} de saldo")
        
        # sai do while
        elif funcionalidade == 4:
            print("Até a próxima!")    
            continuar = 0
    
    
    # categoria social
    elif categoria_passageiro == 3:
        
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n"))
        
        # faz a recarga 
        if funcionalidade == 1:
            recarga = float(input("Digite o valor da recarga: R$"))
            desconto = recarga * (80/100)
            valor_da_recarga = recarga - desconto
            saldo = recarga
            print(f"Você irá pagar R${valor_da_recarga:.2f}")
            
        # faz a compra de passagens
        elif funcionalidade == 2:
            qnt_passagem = int(input("Quantas passagens você quer comprar: "))
            valor_passagem *= qnt_passagem
            if saldo >= valor_passagem:
                print("Compra efetuada com sucesso!")
            else:
                print("Compra mal sucedida, devido a falta de saldo")
                
        # mostra o saldo
        elif funcionalidade == 3:
            if saldo >= valor_da_recarga:
                print(f"Você tem R${saldo:.2f} de saldo")
            else:
                print("Você não tem saldo suficiente!")

        # sai do while
        elif funcionalidade == 4:
            print("Até a próxima!")    
            continuar = 0
    
    # mostra o relatório
    elif categoria_passageiro == 4:
        print("==" * 15, "Relatório", "==" * 15)
        print(f"Total de recargas efetuadas: {recarga_total}\nValor total de recargas: R${recarga_valor_total_1:.2f}")
    
    # categoria saída
    elif categoria_passageiro == 5:
        print("Até a próxima!")    
        continuar = 0
        