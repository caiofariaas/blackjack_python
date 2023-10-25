from jogador import Jogador
from dealer import Dealer

dealer = Dealer(10)

jogadores = []

qtd = int(input("Quantos jogadores vão jogar?: "))

for i in range(qtd):
    nome = input(f"Digite o nome do Jogador {i + 1}: ")
    idade = int(input(f"Digite a idade do Jogador {i + 1}: "))
    jogador = Jogador(nome, idade)
    jogadores.append(jogador)

for jogador in jogadores:
    dealer.distribuirCartas(jogador)

while True:
    for i in range(qtd):
        if jogadores[i].getJogou() == True:
            continue

        print(f"Jogador {i + 1}")
        print(f"Suas cartas : {jogadores[i].getCartas()}")
        print(f"Pontos totais: {jogadores[i].totalCartas()}")
    
        opt = int(input("Deseja comprar mais uma carta? (1 - Sim | 2 - nao ) : "))

        if opt == 1:
            jogadores[i].comprar_cartas(dealer.compra_carta())
            
            if jogadores[i].totalCartas() == 21:
                print(f"O jogador {jogadores[i].nome()} completou 21 e ganhou o jogo!")

            else:

                if jogadores[i].totalCartas() > 21:
                    print(f"Pontos totais: {jogadores[i].totalCartas()}")
                    print(f"Seus pontos ultrapassaram 21, Você perdeu!\n")
                    jogadores[i].parar()

                elif jogadores[i].getJogou() == True:
                    pass
                
                else:
                    print("-=" * 20)
                    print(f"Jogador {i + 1}")
                    print(f"Suas cartas : {jogadores[i].getCartas()}")
                    print(f"Pontos totais: {jogadores[i].totalCartas()}")
                    print("-=" * 20)
                    
                    opt2 = int(input("\nSelecione uma das opções\n1 <- Parar\n2 <- Continuar\nR: "))
                    
                    if opt2 == 1:
                        jogadores[i].parar()
                    elif opt2 == 2:
                        pass
                
        elif opt == 2:
            opt2 = int(input("Selecione uma das opções\n1 <- Parar\n2 <- Continuar\nR: "))
                
            if opt2 == 1:
                jogadores[i].parar()
            elif opt2 == 2:
                pass
            pass
