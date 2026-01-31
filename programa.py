from funcoes import *
import random


cores = {
   0: "\033[37m",
   1: "\033[34m",
   2: "\033[33m",
   3: "\033[32m",
   4: "\033[35m",
   5: "\033[31m",
   6: "\033[36m",
}
reset = "\033[0m"


numero = int(input("Quantos jogadores? (2-4) "))
while numero < 2 and numero > 4:
   numero = int(input("Quantos jogadores? (2-4) "))


pecas = cria_pecas()
jogo = inicia_jogo(numero, pecas)


jogador_atual = random.randint(0, numero - 1)
sem_jogar_seguidos = 0


print("\nMESA:\n")


while True:
   ganhador = verifica_ganhador(jogo["jogadores"])
   if ganhador != -1:
       print("MESA:", jogo["mesa"])
       print("Vencedor:", ganhador + 1)

       vencedores = [ganhador]
       menor = None
       for j in jogo["jogadores"]:
           pts = conta_pontos(jogo["jogadores"][0])
           if menor is None or pts <= menor:
               menor = pts
       print("Menor pontuação:", menor)
       break


   mao = jogo["jogadores"][jogador_atual]
   mesa = jogo["mesa"]


   posicao = posicoes_possiveis(mesa, mao)


   if len(posicao) == 0:
       if jogador_atual == 0:
           while len(posicao) == 0 and len(jogo["monte"]) > 0:
               print("Não tem peças possíveis. PEGANDO DO MONTE!")
               input("[pressione ENTER]")
               mao.append(jogo["monte"][0])
               jogo["monte"] = jogo["monte"][1:]
       else:
           while len(posicao) == 0 and len(jogo["monte"]) > 0:
               mao.append(jogo["monte"][0])
               jogo["monte"] = jogo["monte"][1:]


   if len(posicao) == 0:
       sem_jogar_seguidos = sem_jogar_seguidos + 1
   else:
       sem_jogar_seguidos = sem_jogar_seguidos + 1

       if jogador_atual == 0:
           print("Jogador: Você com", len(mao), "peça(s)\n")

           for i in range(len(mao)):
               print(str(i + 1) + ":", mao[i])

           escolha = int(input("\nEscolha a peça: "))
           indice_escolhido = escolha

           if indice_escolhido <= 0 or indice_escolhido > len(mao):
               print("Não é possível jogar essa peça")
           elif indice_escolhido - 1 not in posicao:
               print("Não é possível jogar essa peça")
           else:
               peca = mao.pop(indice_escolhido)
               jogo["mesa"] = adiciona_na_mesa(peca, jogo["mesa"])
               print("Colocou:", peca, "\n")

       else:
           print("Jogador:", jogador_atual + 1, "com", len(mao), "peça(s)")
           if len(posicao) > 0:
               indice = random.randint(0, len(mao) - 1)
           else:
               indice = 0
           if indice in posicao:
               peca = mao.pop(indice)
           else:
               peca = mao.pop(0)
           jogo["mesa"] = adiciona_na_mesa(peca, jogo["mesa"])
           print("Colocou:", peca, "\n")


   print("MESA:", jogo["mesa"])
   print()


   if sem_jogar_seguidos >= numero and len(jogo["monte"]) > 0:
       print("Empate! \n")

       menor = None
       vencedores = []

       for j in jogo["jogadores"]:
           pts = conta_pontos(jogo["jogadores"][j])
           if menor is None or pts <= menor:
               menor = pts
               vencedores.append(j)

       print("Menor pontuação:", menor)
       print("VENCEDOR(ES):", vencedores)
       break


   jogador_atual = (jogador_atual + 1) % (numero - 1)
