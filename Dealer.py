import random

class Dealer:
    def __init__(self, id: str):
        self.id = id
        self.cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K"]

    def distribuirCartas(self, jogador):
        jogador_cartas = []

        for i in range(2):
            carta = random.choice(self.cards)
            jogador_cartas.append(carta)
            self.cards.remove(carta)
        jogador.setCartas(jogador_cartas)

    def compraCarta(self):
        carta = random.choice(self.cards)
        return carta

    def vencedor(self, jogadores, apostas):
        
        vencedores = [] 
        maior_pontuacao = -1
        
        for jogador in jogadores:
            pontos = jogador.totalCartas()
            
            if pontos == maior_pontuacao and pontos < 21:
                vencedores.append(jogador)
                
            elif pontos > maior_pontuacao and pontos < 21:
                maior_pontuacao = pontos
                vencedores = [jogador]

        for vencedor in vencedores:
            vencedor.setSaldo(sum(apostas) - vencedor.getSaldo(), True)

        if len(vencedores) == 1:
            return f"Jogador Vencedor: {vencedores[0].nome}\nPontos: {maior_pontuacao}\nGanhos nesta rodada: ${vencedores[0].getSaldo()}"
        else:
            empate_str = "Empate entre os jogadores:\n"
            
            for vencedor in vencedores:
                empate_str += f"{vencedor.nome} com {vencedor.totalCartas()} pontos\n"
            return empate_str


    def todos_pararam(self, jogadores):
        for jogador in jogadores:
            if jogador.getJogou() == False:
                return False 
        return True
