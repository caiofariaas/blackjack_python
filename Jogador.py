class Jogador:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.pontos = 0
        self.__cartas = []
        self.jogou = False
        self.__saldo = 3000
        self.__apostou = False

    def comprar_cartas(self, carta):
        self.__cartas.append(carta)

    def getCartas(self):
        return self.__cartas
    
    def setCartas(self, cartas):
        self.__cartas = cartas
        
    def getJogou(self):
        return self.jogou
    
    def parar(self):
        self.jogou = True

# Faz a soma das cartas recebidas pelo dealer
    
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

    def __estorou(self):
        return self.totalCartas() > 21

    def parar_estouro(self):
        if self.__estorou():
            self.jogou = True

    def getSaldo(self):
        return self.__saldo
    
# um Set porem com um valor booleano, caso receba True, o jogador ganhou
#  assim ele adiciona ao seu saldo, caso False ele remove!
    
    def setSaldo(self, newSaldo, tf):
        if tf == True:
            self.__saldo += newSaldo
        elif tf == False:
            self.__saldo -= newSaldo

    def setApostou(self, yn):
        self.__apostou = yn

    def getApostou(self):
        return self.__apostou
