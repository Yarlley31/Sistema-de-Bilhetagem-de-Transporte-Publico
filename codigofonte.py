# titulo
print("Bem-vindo ao Sistema de Bilhetagem de Transporte Público")
print("-" * 30)

# entrada do usuario
valor_passagem = float(input("Digite o valor da passagem: "))
print("-" * 45)

# variaveis
continuar = True
funcionalidade = 0
saldo = 0
valor_a_pagar = 0
recarga = 0

# processamento
while continuar == True:
    categoria_passageiro = int(input("Selecione uma das categorias de passageiro:\n[1] Padrão \n[2] Estudante/Idoso\n[3] Social \n[4] Sair do sistema\n"))
    
    # categoria padrao
    if categoria_passageiro == 1:
        desconto = 0
        funcionalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n"))
        print("-" * 34)
        
        # faz a recarga
        if funcionalidade == 1:
            recarga = float(input("Digite o valor da recarga: R$"))
            saldo = recarga
            print("Recarca efetuada com sucesso")
            print("-" * 40)
            
        # faz a compra de passagens
        elif funcionalidade == 2:
            qnt_passagem = int(input("Quantas passagens você quer comprar: "))
            valor_passagem *= qnt_passagem
            if saldo >= valor_passagem:
                print(f"Compra efetuada com sucesso no valor de R${valor_passagem:.2f}!")
                print("-" * 30)

            else:
                print("Compra mal sucedida, devido a falta de saldo")
                print("-" * 30)

        # mostra o saldo
        elif funcionalidade == 3:
            if recarga == 0:
                print("Você não tem saldo")
                print("-" * 30)
            elif saldo >= recarga:
                print(f"Você tem R${saldo - valor_passagem} de saldo")
                print("-" * 30)
            else:
                print("Você não tem saldo suficiente!")
                print("-" * 30)
                
        # sai do while
        elif funcionalidade == 4:
            continuar = False
        