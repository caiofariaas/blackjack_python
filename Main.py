from Jogador import Jogador
from Dealer import Dealer

dealer = Dealer(10)

jogadores = []
jogadores_final = []

qtd = int(input("Quantos jogadores vão jogar?: "))

for i in range(qtd):
    nome = input(f"Digite o nome do Jogador {i + 1}: ")
    idade = int(input(f"Digite a idade do Jogador {i + 1}: "))
    jogador = Jogador(nome, idade)
    jogadores.append(jogador)

for jogador in jogadores:
    if jogador.idade < 18:
        jogadores.remove(jogador)
        print("-=" * 23)
        print(f"O jogador {jogador.nome} foi removido por ser menor de idade")
        print("-=" * 23)
        qtd = len(jogadores)
        
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

            if jogadores[i].getJogou() == True:
                continue

            print(f"Jogador: {jogadores[i].nome}")
            print(f"Suas cartas : {jogadores[i].getCartas()}")
            print(f"Pontos totais: {jogadores[i].totalCartas()}")
        
            opt = int(input("Deseja comprar mais uma carta? (1 - Sim | 2 - nao ) : "))

            if opt == 1:
                jogadores[i].comprar_cartas(dealer.compraCarta())
                
                if jogadores[i].totalCartas() == 21:
                    print(f"O jogador {jogadores[i].nome} completou 21 e ganhou o jogo!")
                    exit()

                elif jogadores[i].totalCartas() > 21:
                    print(f"Pontos totais: {jogadores[i].totalCartas()}")
                    print(f"Seus pontos ultrapassaram 21, Você perdeu!\n")
                    jogadores[i].parar()
                    

                elif jogadores[i].getJogou() == True:
                    pass
                
                else:
                    print("-=" * 20)
                    print(f"Jogador: {jogadores[i].nome}")
                    print(f"Suas cartas : {jogadores[i].getCartas()}")
                    print(f"Pontos totais: {jogadores[i].totalCartas()}")
                    print("-=" * 20)
                    
                    opt2 = int(input("\nSelecione uma das opções\n1 <- Parar\n2 <- Continuar\nR: "))
                    
                    if opt2 == 1:
                        jogadores[i].parar()
                        print("-" * 26)
                        print(f"O jogador {jogadores[i].nome} parou!")
                        print("-" * 26)

                    elif opt2 == 2:
                        pass
                    
            elif opt == 2:
                opt2 = int(input("Selecione uma das opções\n1 <- Parar\n2 <- Continuar\nR: "))
                    
                if opt2 == 1:
                    jogadores[i].parar()
                    print("-" * 26)
                    print(f"O jogador {jogadores[i].nome} parou!")
                    print("-" * 26)
                    
                elif opt2 == 2:
                    pass
