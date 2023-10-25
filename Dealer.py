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

    def __vencedor(self, jogadores):
        vencedor = None
        maior_pontuacao = -1
        
        for jogador in jogadores:
            pontos = jogador.totalCartas()
            if pontos > maior_pontuacao:
                maior_pontuacao = pontos
                vencedor = jogador
        return jogador
