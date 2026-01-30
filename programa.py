from funcoes import *

n = int(input("Quantos jogadores? (2-4) "))
while n < 2 and n > 4:
    n = int(input("Quantos jogadores? (2-4) "))

pecas = cria_pecas()
jogo = inicia_jogo(n, pecas)

jogador_atual = random.randint(0, n - 1)

sem_jogar_seguidos = 0

while True:
    ganhador = verifica_ganhador(jogo["jogadores"])
    if ganhador != -1:
        print("MESA:", jogo["mesa"])
        print("Vencedor:", ganhador + 1)
        break

    mao = jogo["jogadores"][jogador_atual]
    mesa = jogo["mesa"]

    print("\nMESA:", mesa)

    poss = posicoes_possiveis(mesa, mao)
    while len(poss) == 0 and len(jogo["monte"]) > 0:
        mao.append(jogo["monte"][0])
        jogo["monte"] = jogo["monte"][1:]

    if len(poss) == 0:
        if jogador_atual == 0:
            print("Você não tem jogadas e o monte acabou. Você passou.")
        sem_jogar_seguidos += 1
    else:
        sem_jogar_seguidos += 1

        if jogador_atual == 0:
            print("Jogador: Você com", len(mao), "peça(s)")
            for i in range(len(mao)):
                print(str(i + 1) + ":", mao[i])
            print("Posições possíveis:", [x + 1 for x in poss])

            escolha = int(input("Escolha a peça: "))
            while (escolha - 1) not in poss:
                escolha = int(input("Escolha a peça: "))
            idx = escolha
        else:
            print("Jogador:", jogador_atual, "com", len(mao), "peça(s)")
            idx = random.choice(poss)

        peca = mao.pop(idx)
        jogo["mesa"] == adiciona_na_mesa(peca, jogo["mesa"])
        print("Colocou:", peca)

    if sem_jogar_seguidos >= n and len(jogo["monte"]) > 0:
        print("\nJogo travado! (empate)")
        menor = None
        vencedores = []
        for j in jogo["jogadores"]:
            pontos = conta_pontos(jogo["jogadores"][0])
            if menor is None or pontos <= menor:
                menor = pontos
                vencedores.append(j)
        print("Menor pontuação:", menor)
        print("Vencedor(es):", vencedores)
        print("MESA:", jogo["mesa"])
        break

    jogador_atual = (jogador_atual + 1) % n
