from teste.Dominio.time import *

j1 = Jogador('Messi', 10, 'Segundo  Atacante', 94)
j2 = Jogador('Cristiano Ronaldo', 7, 'Ponta Esquerda', 92)
j3 = Jogador('Lukako', 9, 'Centroavante', 88)
j4 = Jogador('Bastoni', 95 , 'Zagueiro', 80)
j5 = Jogador('pessina', 22, 'Meio-campo', 75)

j1.status_jogador()
j1.sofre_lesao()
j1.status_jogador()
j1.treinamento()
j1.status_jogador()
aplicar_cartoes(j1, 2)
j1.status_jogador()

j4.status_jogador()
j4.sofre_lesao()
j4.status_jogador()
j4.treinamento()
j4.status_jogador()
aplicar_cartoes(j4, 5)
j4.status_jogador()

