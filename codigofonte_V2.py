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
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Verificar saldo\n[3] Sair do sistema\n"))
        print("-" * 30)
        if funcionalidade == 1:
            recarga = float(input("Digite o valor da recarga: R$"))
            saldo = recarga
            valor_a_pagar = recarga
            print(f"Você irá pagar R${valor_a_pagar:.2f}")
            print("-" * 30)
        
        elif funcionalidade == 2:
            if saldo >= valor_a_pagar:
                print(f"Você tem R${saldo:.2f} de saldo")
                print("-" * 30)
            else:
                print("Você não tem saldo suficiente!")
        elif funcionalidade == 3:
            break
        
    # categoria estudante/idoso
    elif categoria_passageiro == 2:
        
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Verificar saldo \n[3] Sair do sistema\n"))
        if funcionalidade == 1:
            recarga = float(input("Digite o valor da recarga: R$"))
            desconto = recarga / 2
            valor_a_pagar = recarga - desconto
            saldo = recarga
            print(f"Você irá pagar R${valor_a_pagar:.2f}")
        elif funcionalidade == 2:
            if saldo >= valor_a_pagar:
                print(f"Você tem R${saldo:.2f} de saldo")
                print("-" * 30)
            else:
                print("Você não tem saldo suficiente!")
        elif funcionalidade == 3:
            break
    
    
    # categoria social
    elif categoria_passageiro == 3:
        
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Verificar saldo\n[3] Sair do sistema\n"))
        if funcionalidade == 1:
            recarga = float(input("Digite o valor da recarga: R$"))
            desconto = recarga * (80/100)
            valor_a_pagar = recarga - desconto
            saldo = recarga
            print(f"Você irá pagar R${valor_a_pagar:.2f}")
            
        elif funcionalidade == 2:
            if saldo >= valor_a_pagar:
                print(f"Você tem R${saldo:.2f} de saldo")
                print("-" * 30)
            else:
                print("Você não tem saldo suficiente!")
        
        elif funcionalidade == 3:
            break
        
    # categoria saída
    elif categoria_passageiro == 4:
        print("Até a próxima!")    
        break
        