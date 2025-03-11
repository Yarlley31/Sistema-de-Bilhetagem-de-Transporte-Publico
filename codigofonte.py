# menu inicial
print("Bem-vindo ao Sistema de Bilhetagem de Transporte Público")
continuar = True
while continuar == True:
    categoria_passageiro = int(input("Selecione uma das categorias de passageiro:\n[1] padrão \n[2] estudante/idoso\n[3] social \n"))
    valor_da_passagem = float(input("Digite o valor da passagem: "))
    if categoria_passageiro == 1:
        desconto = 0
        valor_final = valor_da_passagem
        print(f'O valor da passagem será: R${valor_final:.2f}')
    elif categoria_passageiro == 2:
        desconto = valor_da_passagem / 2
        valor_final = valor_da_passagem - desconto
        print(f"o valor da passagem será R${valor_final:.2f}")
    elif categoria_passageiro == 3:
        desconto = valor_da_passagem 
        valor_final = valor_da_passagem * 0.2
        print(f"o valor da passagem será R${valor_final:.2f}")
    
    
    funiconalidade = int(input("Selecione uma de nossas funcionalidades: \n[1] Recarga \n[2] Comprar passagem \n[3] Sair do sistema\n"))
    if funiconalidade == 1:
        saldo = float(input("Digite o valor da recarga: R$"))
    elif funiconalidade == 2:
        qnts_passagem = int(input("Digite quantas passagem deseja comprar: "))
        preco_total = qnts_passagem * valor_final
        print(preco_total)
    # continuar = input("você desejsa sair? [S/N]")
    # if continuar == "S":
    #     break
    # else:
    #     continue