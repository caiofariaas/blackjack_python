from Jogador import Jogador
from Dealer import Dealer

# Funções.

def prntVencedor():
    print("\n")
    print("-=" * 16)
    print(f"\n{dealer.vencedor(jogadores, apostas)}\n")
    print("-=" * 16)
    print("\n")
    exit()

def prntJogador():
    print(f"\nJogador: {jogadores[i].nome}")
    print(f"Suas cartas : {jogadores[i].getCartas()}")
    print(f"Pontos totais: {jogadores[i].totalCartas()}")
    print(f"Seu Saldo: ${jogadores[i].getSaldo()}\n")

# Criação de listas e declaração do dealer.

dealer = Dealer(10)
jogadores = []
jogadores_final = []
apostas = []

# Início.
# Criação dos jogadores.

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
print("-" * 50)

for i in range(qtd):
    if jogadores[i].idade >= 18:
        jogadores_final.append(jogadores[i]) 
    
    else:
        print(f"O jogador {jogadores[i].nome} foi removido por ser menor de idade")
        
print('-' * 50)
        
jogadores = jogadores_final
jogadores_ativos = jogadores.copy()
        
if len(jogadores) == 0 or len(jogadores) == 1:
    print("-=" * 19)
    print(f"\nNão é possivel jogar com {len(jogadores)} jogadores!\n")
    print("-=" * 19)
    exit()

# Distribuição das cartas.

else:
    print("\n🃏 Seja bem vindo ao Blackjack! 🃏")
    for jogador in jogadores:
        card = dealer.distribuirCartas(jogador)


    while True:
        for i in range(qtd):
            
# Caso Restar apenas 1 jogador e o status dele por True.

            if len(jogadores_ativos) == 1 and jogadores_ativos[0].jogou == True:
                print(f"{jogadores[i].nome}")
                print("-" * 26)
                print(f"{dealer.vencedor(jogadores, apostas)}")
                print("-" * 26)
                exit()

            if jogadores[i].getJogou() == True:
                continue
                 
            prntJogador()

            if jogadores[i].getApostou() == False:

# Aposta.

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
                        jogadores[i].setSaldo(aposta, False)
                        print(f"Saldo Restante: ${jogadores[i].getSaldo()}\n")
                        break
                    
                    except(ValueError):
                        print("-=" * 20)
                        print("\nValor inválido!, digite um número.\n")
                        print("-=" * 20)

            while True:
                try:
                    opt = int(input("Deseja comprar mais uma carta?\n1 <- Sim\n2 <- Não\nR: "))
                    break
                
                except(ValueError):
                    print("-=" * 20)
                    print("\nValor inválido!, digite um valor inteiro.\n")
                    print("-=" * 20)

# Comprar Cartas.

            if opt == 1:
                jogadores[i].comprar_cartas(dealer.compraCarta())
                
                if jogadores[i].totalCartas() == 21:
                    jogadores[i].setSaldo(sum(apostas) - jogadores[i].getSaldo(), True)
                    print("\n")
                    print("-=" * 20)
                    print(f"O jogador {jogadores[i].nome} completou 21 e ganhou o jogo!\nGanhos da rodada: ${jogadores[i].getSaldo()}\nCartas: {jogadores[i].getCartas()}")
                    print("-=" * 20)
                    print("\n")
                    exit()

# Caso os pontos do jogador ultrapassem 21.

                elif jogadores[i].totalCartas() > 21:
                    print("-" * 40)

                    prntJogador()
                    
                    print(f"Seus pontos ultrapassaram 21, Você perdeu!\n")
                    print("-" * 40)
                    jogadores[i].parar_estouro()
                    jogadores_ativos.remove(jogadores[i])   
                         
# Apenas mostro os status do jogador novamente após a compra de cartas.

                else:
                    prntJogador()

# Parar ou continuar no jogo.

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
                        print("\n")
                        print("-" * 26)
                        print(f"O jogador {jogadores[i].nome} parou!")
                        print("-" * 26)
                        jogadores_ativos.remove(jogadores[i])

                    elif opt2 == 2:
                        continue
                       
            elif opt == 2:
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
                    print("\n")
                    print("-" * 26)
                    print(f"O jogador {jogadores[i].nome} parou!")
                    print("-" * 26)
                    jogadores_ativos.remove(jogadores[i])
                    
                elif opt2 == 2:
                    continue
                
# Verificação sobre quem foi o jogador vencedor.

                if dealer.todos_pararam(jogadores) == True:
                    prntVencedor()

                elif len(jogadores) == 2:
                    if jogadores[i].totalCartas() > 21:
                        prntVencedor()

            if dealer.todos_pararam(jogadores) == True:
                prntVencedor()

            elif len(jogadores) == 2:
                if jogadores[i].totalCartas() > 21:
                    prntVencedor()
