from Jogador import jogador
from Dealer import Dealer




dealer = Dealer(10, )

for i in range (2):
    nome = input(f"Digite o nome do Jogador {i + 1}: ")
    idade = int(input(f"Digite a idade do Jogador {i + 1}: "))

    if i == 0:
        jogador1 = jogador(nome, idade)
    elif i == 1:
        jogador2 = jogador(nome, idade)

print(jogador1.idade)
print(jogador2.idade)
