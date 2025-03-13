# menu inicial
print("Bem-vindo ao Sistema de Bilhetagem de Transporte Público")
valor_passagem = float(input("insira o valor da passagem: "))
print("-" * 30)

# variaveis
continuar = True
funcionalidade = 0
saldo = 0
valor_a_pagar = 0

while continuar == True:
    categoria_passageiro = int(input("Selecione uma das categorias de passageiro:\n[1] padrão \n[2] estudante/idoso\n[3] social \n[4] Sair do sistema\n"))
    print("-" * 30)
    
    # categoria padrão
    if categoria_passageiro == 1:
        desconto = 0
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n"))
        print("-" * 30)
        
        # faz a recarga
        if funcionalidade == 1:
            recarga = float(input("Digite o valor da recarga: R$"))
            saldo = recarga
            print("Recarca efetuada com sucesso")
            print("-" * 30)
            
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
            if saldo >= recarga:
                print(f"Você tem R${saldo - valor_passagem} de saldo")
                print("-" * 30)
            else:
                print("Você não tem saldo suficiente!")
                
        # sai do while
        elif funcionalidade == 4:
            break
        
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
            break
    
    
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
                print("-" * 30)
            else:
                print("Você não tem saldo suficiente!")

        # sai do while
        elif funcionalidade == 4:
            break
        
    # categoria saída
    elif categoria_passageiro == 4:
        print("Até a próxima!")    
        break
        