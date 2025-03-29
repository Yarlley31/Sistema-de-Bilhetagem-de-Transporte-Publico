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

# saldo de cada categoria

saldo1 = 0
saldo2 = 0
saldo3 = 0

# número de recargas realizadas por cada user
num_recargas_1 = 0
num_recargas_2 = 0
num_recargas_3 = 0

qntd_recarga_total = 0

# número de passagens usados por cada user
qntd_passagem_1 = 0
qntd_passagem_2 = 0
qntd_passagem_3 = 0

# valor total gasto com passagens por cada user
valor_total_gasto_passagem_1 = 0
valor_total_gasto_passagem_2 = 0
valor_total_gasto_passagem_3 = 0

# saldo restante de cada user
saldo_restante_1 = 0
saldo_restante_2 = 0
saldo_restante_3 = 0

while continuar == 1:

    categoria = input("Selecione uma das categorias:\n[1] padrão \n[2] estudante/idoso\n[3] social \n[4] Relatório \n[5] Sair do sistema\n")
    while categoria.isdigit() == False:
        categoria = input("Selecione uma das categorias:\n[1] padrão \n[2] estudante/idoso\n[3] social \n[4] Relatório \n[5] Sair do sistema\n")
        
    categoria = int(categoria)
    
    # categoria padrão
    if categoria == 1:

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
            
            print("Recarga efetuada com sucesso")
            saldo1 += recarga
            num_recargas_1 += 1
            qntd_recarga_total += 1
            
        # faz a compra de passagens
        elif funcionalidade == 2:
            qntd_passagem_1 = input("Quantas passagens você quer comprar: ")
            while qntd_passagem_1.isdigit() == False:
                qntd_passagem_1 = input("Quantas passagens você quer comprar: ")
            qntd_passagem_1 = int(qntd_passagem_1)
            
            
            valor_passagem *= qntd_passagem_1
            valor_total_gasto_passagem_1 += valor_passagem
            if saldo1 >= valor_passagem:
                print("Compra efetuada com sucesso!")
                saldo1 -= valor_passagem
            else:
                print("Compra mal sucedida, devido a falta de saldo")
            
                
        # mostra o saldo
        elif funcionalidade == 3:
            print(f"E seu saldo é: R${saldo1:.2f}")
            if saldo1 >= valor_passagem:
                print(f"Você tem saldo suficiente para embarcar!")
            else:
                print("Você não tem saldo suficiente!")
                print(f"Seu saldo é: R${saldo1:.2f}")
        
        # sai do while
        elif funcionalidade == 4:
            print("Até a próxima")
            continuar = 0
        
        saldo_restante_1 = saldo1
        
    # categoria estudante/idoso
    elif categoria == 2:
        
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
            print("Recarga efetuada com sucesso!")
            
            saldo2 += recarga
            num_recargas_2 += 1
            qntd_recarga_total += 1

        
        # faz a compra de passagens
        elif funcionalidade == 2:
            qntd_passagem_2 = input("Quantas passagens você quer comprar: ")
            while qntd_passagem_2.isdigit() == False:
                qntd_passagem_2 = input("Quantos passagem você quer comprar: ")
            qntd_passagem_2 = int(qntd_passagem_2)
            valor_passagem = (valor_passagem / 2) * qntd_passagem_2
            
            valor_total_gasto_passagem_2 += valor_passagem

            if saldo2 >= valor_passagem:
                print(f"Compra efetuada com sucesso!")
                saldo2 -= valor_passagem
            else:
                print("Compra mal sucedida, devido a falta de saldo")
            
        
        # mostra o saldo
        elif funcionalidade == 3:
            print(f"E seu saldo é: R${saldo2:.2f}")
            if saldo2 >= valor_passagem:
                print(f"Você tem saldo suficiente para embarcar!")
                saldo2 -= valor_passagem
                saldo_restante_2 = saldo2
            else:
                print("Você não tem saldo suficiente!")
                print(f"Seu saldo é: R${saldo2:.2f}")
        
        # sai do while
        elif funcionalidade == 4:
            print("Até a próxima!")   
            continuar = 0
             
        saldo_restante_2 = saldo2

    # categoria social
    elif categoria == 3:


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
            saldo3 += recarga
            print("Recarga efetuada com sucesso!")
            
            num_recargas_3 += 1
            qntd_recarga_total += 1
            
        # faz a compra de passagens
        elif funcionalidade == 2:
            qntd_passagem_3 = int(input("Quantas passagens você quer comprar: "))
            valor_passagem = (valor_passagem * 0.20) * qntd_passagem_3
            
            valor_total_gasto_passagem_3 += valor_passagem
            
            if saldo3 >= valor_passagem:
                print("Compra efetuada com sucesso!")
                saldo3 -= valor_passagem
            else:
                print("Compra mal sucedida, devido a falta de saldo")
            
                
        # mostra o saldo
        elif funcionalidade == 3:
            print(f"E seu saldo é: R${saldo3:.2f}")
            if saldo3 >= valor_passagem:
                print(f"Você tem saldo suficiente para embarcar!")
            else:
                print("Você não tem saldo suficiente!")
                print(f"Seu saldo é: R${saldo3:.2f}")

        # sai do while
        elif funcionalidade == 4:
            print("Até a próxima!")    
            continuar = 0
    
        saldo_restante_3 = saldo3
        
    # mostra o relatório
    elif categoria == 4:
        print("==" * 15, "Relatório", "==" * 15)
        
        print(f"Quantidade de recargas total: {qntd_recarga_total}")
        print(f"Número de recargas realizadas por cada categoria: \nPadrão: {num_recargas_1}\nEstudante/Idoso: {num_recargas_2}\nSocial: {num_recargas_3}")
        print("-" * 35)
        print(f"Quantidade passagens compradas por cada categoria: \nPadão: {qntd_passagem_1}\nEstudante/Idoso: {qntd_passagem_2}\nSocial: {qntd_passagem_3}")
        print("-" * 35)
        print(f"Valor total gasto em passagem por cada categoria: \nPadão: {valor_total_gasto_passagem_1:.2f}\nEstudante/Idoso: {valor_total_gasto_passagem_2:.2f}\nSocial: {valor_total_gasto_passagem_3:.2f}")
        print("-" * 35)
        print(f"O saldo restante de cada categoria é: \nPadão: {saldo_restante_1:.2f}\nEstudante/Idoso: {saldo_restante_2:.2f}\nSocial: {saldo_restante_3:.2f}")
        print("-" * 35)


    # categoria saída
    elif categoria == 5:
        print("Até a próxima!")    
        continuar = 0
        