from Jogador import Jogador
from Dealer import Dealer

dealer = Dealer(10)

jogadores = []
jogadores_final = []
apostas =[]

while True:
    try:
        qtd = int(input("Quantos jogadores vão jogar?: "))
        if qtd == 1 or qtd == 0:
            print("-=" * 20)
            print("Não é possivel jogar com 0 ou 1 Jogadores!")
            print("-=" * 20)
            continue
        break

    except(ValueError):
        print("-=" * 20)
        print("Valor inválido!, digite um valor inteiro.")
        print("-=" * 20)

for i in range(qtd):
    nome = input(f"Digite o nome do Jogador {i + 1}: ")
    while True:
        try:
            idade = int(input(f"Digite a idade do Jogador {i + 1}: "))
            break
        except(ValueError):
            print("-=" * 20)
            print("Valor inválido!, digite um valor inteiro.")
            print("-=" * 20)

    jogador = Jogador(nome, idade)
    jogadores.append(jogador)

for i in range(qtd):
    if jogadores[i].idade >= 18:
        jogadores_final.append(jogadores[i]) 
    else:
        print("-=" * 25)
        print(f"O jogador {jogadores[i].nome} foi removido por ser menor de idade")
        print("-=" * 25)

jogadores = jogadores_final
        
if len(jogadores) == 0:
    print("-=" * 19)
    print("\nNão é possivel jogar com 0 jogadores!\n")
    print("-=" * 19)
    exit()
    
else:
    for jogador in jogadores:
        card = dealer.distribuirCartas(jogador)

    while True:
        for i in range(qtd):

            if qtd == 1 and jogadores[i].getJogou() == True:
                print("-" * 26)
                print("Todos os jogadores pararam!")
                print(f"{dealer.vencedor(jogadores, apostas)} !")
                print("-" * 26)
                exit()

            if jogadores[i].getJogou() == True:
                continue
                
            print(f"Jogador: {jogadores[i].nome}")
            print(f"Suas cartas : {jogadores[i].getCartas()}")
            print(f"Pontos totais: {jogadores[i].totalCartas()}")
            print(f"Seu Saldo: ${jogadores[i].getSaldo()}")
            if jogadores[i].getApostou() == False:
                while True:
                    try:
                        aposta = float(input("Digite o valor de sua aposta: "))
                        if aposta > jogadores[i].getSaldo():
                            print("-=" * 20)
                            print("Você não possui esse valor em sua carteira!")
                            print("-=" * 20)
                            continue
                        
                        jogadores[i].setApostou(True)
                        apostas.append(aposta)
                        break
                    except:
                        print("Valor inválido, Digite um número!")

            while True:
                try:
                    opt = int(input("Deseja comprar mais uma carta? (1 - Sim | 2 - nao ) : "))
                    break
                except(ValueError):
                    print("-=" * 20)
                    print("Valor inválido!, digite um valor inteiro.")
                    print("-=" * 20)
                    
            if opt == 1:
                jogadores[i].comprar_cartas(dealer.compraCarta())
                
                if jogadores[i].totalCartas() == 21:
                    jogadores[i].setSaldo(sum(apostas) - jogadores[i].getSaldo(), True)
                    print(f"O jogador {jogadores[i].nome} completou 21 e ganhou o jogo!\nSaldo Final: ${jogadores[i].getSaldo()}")
                    exit()

                elif jogadores[i].totalCartas() > 21:
                    print(f"Jogador: {jogadores[i].nome}")
                    print(f"Pontos totais: {jogadores[i].totalCartas()}")
                    print(f"Seus pontos ultrapassaram 21, Você perdeu!\n")
                    jogadores[i].parar_estouro()
                    qtd -= 1


                elif jogadores[i].getJogou() == True:
                    pass
                
                else:
                    print("-=" * 20)
                    print(f"Jogador: {jogadores[i].nome}")
                    print(f"Suas cartas : {jogadores[i].getCartas()}")
                    print(f"Pontos totais: {jogadores[i].totalCartas()}")
                    print("-=" * 20)
                    
                    while True:
                        try:
                            opt2 = int(input("\nSelecione uma das opções\n1 <- Parar\n2 <- Continuar\nR: "))
                            break
                        except(ValueError):
                            print("-=" * 20)
                            print("Valor inválido!, digite um valor inteiro.")
                            print("-=" * 20)

                    if opt2 == 1:
                        jogadores[i].parar()
                        print("-" * 26)
                        print(f"O jogador {jogadores[i].nome} parou!")
                        print("-" * 26)
                        qtd -= 1
                       
            elif opt == 2:
                while True:
                    try:
                        opt2 = int(input("Selecione uma das opções\n1 <- Parar\n2 <- Continuar\nR: "))
                        break
                    except(ValueError):
                        print("-=" * 20)
                        print("Valor inválido!, digite um valor inteiro.")
                        print("-=" * 20)

                if opt2 == 1:
                    jogadores[i].parar()
                    print("-" * 26)
                    print(f"O jogador {jogadores[i].nome} parou!")
                    print("-" * 26)
                    qtd -= 1
                    
                elif opt2 == 2:
                    print("a")

                if dealer.todos_pararam(jogadores) == True:
                    print("-" * 26)
                    print("Todos os jogadores pararam!")
                    print(f"{dealer.vencedor(jogadores, apostas)} !")
                    print("-" * 26)
                    exit()

            if dealer.todos_pararam(jogadores) == True:
                print("-" * 26)
                print("Todos os jogadores pararam!")
                print(f"{dealer.vencedor(jogadores, apostas)} !")
                print("-" * 26)
                exit()
