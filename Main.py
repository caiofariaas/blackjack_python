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



for i in range(qtd):
    print(f"Jogador {i + 1}")
    print(f"Suas cartas : {jogadores[i].getCartas()}")
    print(f"Pontos totais: {jogadores[i].totalCartas()}")
    while True:
        opt = int(input("Deseja comprar mais uma carta? (1 - Sim | 2 - nao) : "))

        if opt == 1:
            jogadores[i].comprar_cartas(dealer.compraCarta())

            if jogadores[i].totalCartas() > 21:
                print(f"Pontos totais: {jogadores[i].totalCartas()}")
                print(f"Seus pontos ultrapassaram 21, Você perdeu!")
                break
            else:
                print("-=" * 20)
                print(f"Jogador {i + 1}")
                print(f"Suas cartas : {jogadores[i].getCartas()}")
                print(f"Pontos totais: {jogadores[i].totalCartas()}")
                print("-=" * 20)

        elif opt == 2:
            pass
