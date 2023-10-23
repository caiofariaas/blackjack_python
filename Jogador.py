class Jogador:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.pontos = 0
        self.__cartas = []
        self.jogou = False

    def comprar_cartas(self, carta):
        self.__cartas.append(carta)

    def getCartas(self):
        return self.__cartas
    
    def setCartas(self, cartas):
        self.__cartas = cartas

    def getJogou(self):
        return self.jogou
    
    def totalCartas(self):
        valorTotal = 0
        for carta in self.__cartas:
            if carta in ["Q", "J", "K"]:
                valorTotal += 10
            elif carta == "A":
                 valorTotal += 1
            else:
                valorTotal += carta
        return valorTotal
