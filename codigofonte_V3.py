"""
Autor: Yarlley Fernandes dos Santos
Componente Curricular: Algoritmos I
Concluido em: 14/10/2011
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

# menu inicial
valor_passagem = input("insira o valor da passagem: ")
while valor_passagem.isdigit() == False:
    valor_passagem = input("Digite o valor em reais da passagem: R$ ")
    
valor_passagem = float(valor_passagem)

# declaração de variáveis
continuar = 1
funcionalidade = 0
valor_a_pagar = 0
recarga_total = 0
saldo = 0
recarga_valor_total_1 = 0

while continuar == 1:

    categoria_passageiro = input("Selecione uma das categorias de passageiro:\n[1] padrão \n[2] estudante/idoso\n[3] social \n[4] Sair do sistema\n")
    while categoria_passageiro.isdigit() == False:
        categoria_passageiro = input("Selecione uma das categorias de passageiro:\n[1] padrão \n[2] estudante/idoso\n[3] social \n[4] Sair do sistema\n")
        
    categoria_passageiro = int(categoria_passageiro)
    
    # categoria padrão
    if categoria_passageiro == 1:

        funcionalidade = input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n")
        while funcionalidade.isdigit() == False:
            print("Você selecionou uma funcionalidade errada.")
            funcionalidade = input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n")
        funcionalidade = int(funcionalidade)
        
        # faz a recarga
        if funcionalidade == 1:
            recarga_total += 1
            
            recarga = input("Digite o valor da recarga: R$")
            while recarga.isdigit() == False:
                recarga = input("Digite o valor da recarga: R$")
            recarga = float(recarga)
            recarga_valor_total_1 = 0
            recarga_valor_total_1 += recarga
            print("Recarga efetuada com sucesso")
            saldo += recarga
            
        # faz a compra de passagens
        elif funcionalidade == 2:
            qnt_passagem_1 = input("Quantas passagens você quer comprar: ")
            while qnt_passagem_1.isdigit() == False:
                qnt_passagem_1 = input("Quantas passagens você quer comprar: ")
            qnt_passagem_1 = int(qnt_passagem_1)
            
            
            valor_passagem *= qnt_passagem_1
            valor_total_passagem_1 = valor_passagem
            if saldo >= valor_passagem:
                print("Compra efetuada com sucesso!")
                saldo -= valor_passagem
            else:
                print("Compra mal sucedida, devido a falta de saldo")
                
        # mostra o saldo
        elif funcionalidade == 3:
            if saldo >= valor_passagem:
                print(f"Você tem saldo suficiente para embarcar!")
                print(f"E seu saldo é: R${saldo:.2f}")
            else:
                print("Você não tem saldo suficiente!")
                print(f"Seu saldo é: R${saldo:.2f}")
        
        # sai do while
        elif funcionalidade == 4:
            print("Até a próxima")
            continuar = 0
        
    # categoria estudante/idoso
    elif categoria_passageiro == 2:
        
        funcionalidade = input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n")
        while funcionalidade.isdigit() == False:
            print("Você selecionou uma funcionalidade errada.")
            funcionalidade = input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n")
        funcionalidade = int(funcionalidade)
        
        # faz a recarga
        if funcionalidade == 1:
            recarga = input("Digite o valor da recarga: R$")
            while recarga.isdigit() == False:
                recarga = input("Digite o valor da recarga: R$")
            recarga = float(recarga)
            saldo += recarga
            print("Recarga efetuada com sucesso!")
            recarga_total += 1
        
        # faz a compra de passagens
        elif funcionalidade == 2:
            qnt_passagem = int(input("Quantas passagens você quer comprar: "))
            valor_passagem = (valor_passagem / 2) * qnt_passagem 
            if saldo >= valor_passagem:
                print(f"Compra efetuada com sucesso!")
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


        funcionalidade = input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n")
        while funcionalidade.isdigit() == False:
            print("Você selecionou uma funcionalidade errada.")
            funcionalidade = input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagens\n[3] Verificar saldo\n[4] Sair do sistema\n")
        funcionalidade = int(funcionalidade)
        
        # faz a recarga 
        if funcionalidade == 1:
            recarga = input("Digite o valor da recarga: R$")
            while recarga.isdigit() == False:
                recarga = input("Digite o valor da recarga: R$")
            recarga = float(recarga)
            
            recarga_total += 1
            
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
            if saldo >= valor_passagem:
                print(f"Você tem saldo suficiente para embarcar!")
                print(f"E seu saldo é: R${saldo:.2f}")
            else:
                print("Você não tem saldo suficiente!")
                print(f"Seu saldo é: R${saldo:.2f}")

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
        