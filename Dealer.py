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
        jogador.setCartas(jogador_cartas)
    
    def compraCarta(self):
        carta = random.choice(self.cards)
        return carta
    