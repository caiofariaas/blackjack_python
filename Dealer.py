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
        vencedor = None
        maior_pontuacao = -1
        
        for jogador in jogadores:
            pontos = jogador.totalCartas()
            if pontos > maior_pontuacao and pontos < 21:
                maior_pontuacao = pontos
                vencedor = jogador

        vencedor.setSaldo(sum(apostas) - vencedor.getSaldo(), True)
        return f"Jogador Vencedor: {vencedor.nome}\nPontos: {maior_pontuacao}\nGanhos nesta rodada: ${vencedor.getSaldo()}"

    def todos_pararam(self, jogadores):
        for jogador in jogadores:
            if jogador.getJogou() == False:
                return False 
        return True
