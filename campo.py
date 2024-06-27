import random         # para gerar números aleatórios
import sys            # para encerrar o programa
import time           # para gerar paradas temporárias
import os             # para executar funções do sistema operacional

field = []     # campo total
mine = []      # local das minas

size = 5      # tamanho do tabuleiro/número de bombas

bomb = "💣"
empty = "⬛"
default = "⬜"
tempBomb = "❌"
tempField = "🟥"

score = 0
posicao = 0

def iniciarJogo():
    os.system("cls")    
    print("")
    print("Boas-vindas ao Campo Minado!")
    print("")
    print("01 - Iniciar o Jogo")
    print("02 - Ver Ranking")
    print("03 - Regras e Instruções")
    print("04 - Sair do Jogo")
    
    opcao = input("O que você deseja fazer? ")

    if opcao == "1" or opcao == "01":
        nome, hora_inicial = gameStart()  # Inicia o jogo e captura nome e hora inicial
        setTable()
        setBomb()
        inputUser(nome, hora_inicial)  # Passa nome e hora inicial para a função que gerencia as jogadas
    elif opcao == "2" or opcao == "02":
        showRank()
    elif opcao == "3" or opcao == "03":
        showRules()
    elif opcao == "4" or opcao == "04":
        print("Obrigado por jogar. Volte sempre!")
        time.sleep(1)
        sys.exit()

def gameStart():
    global score
    score = 0
    nome = input("Insira o seu nome: ")
    hora_inicial = time.time()
    return nome, hora_inicial

def registerRank(nome, hora_inicial, hora_final):
    global score
    tempo = hora_final - hora_inicial

    jogadores = []
    acertos = []
    tempos = []

    if os.path.isfile("ranking.txt"):
        with open("ranking.txt", "r") as arq:
            dados = arq.readlines()
    else:
        dados = []

    for linha in dados:
        partes = linha.strip().split(";")
        jogadores.append(partes[0])
        acertos.append(int(partes[1]))
        tempos.append(float(partes[2]))

    jogadores.append(nome)
    acertos.append(score)
    tempos.append(tempo)

    juntas = sorted(zip(acertos, tempos, jogadores), key=lambda x: (-x[0], x[1]))
    acertos2, tempos2, jogadores2 = zip(*juntas)

    with open("ranking.txt", "w") as arq:
        for jogador, acerto, tempo in zip(jogadores2, acertos2, tempos2):
            arq.write(f"{jogador};{acerto};{tempo:.3f}\n")

def showRank():
    global posicao
    posicao = 0

    if os.path.isfile("ranking.txt"):
        with open("ranking.txt", "r") as arq:
            dados = arq.readlines()
        
        os.system("cls")
        print("Ranking dos Jogadores:")
        print(f"{'Posição':>7} {'Nome':>20} {'Acertos':>10} {'Tempo (s)':>12}")

        for linha in dados:
            posicao += 1
            partes = linha.strip().split(";")
            jogador, acerto, tempo = partes[0], int(partes[1]), float(partes[2])
            print(f"{posicao:>7} {jogador:>20} {acerto:>10} {tempo:>12.3f}")

        input("\nPressione Enter para voltar ao menu...")
        iniciarJogo()
    else:
        print("Nenhum ranking disponível. Jogue uma partida primeiro.")
        time.sleep(2)
        iniciarJogo()

def showRules():
    os.system("cls")
    print("Regras e Instruções do Campo Minado:")
    print("1. O objetivo do jogo é revelar todos os quadrados que não contêm bombas.")
    print("2. Se você revelar um quadrado contendo uma bomba, você perde.")
    print("3. Se você revelar um quadrado vazio, ele mostrará o número de bombas adjacentes.")
    print("4. Use essa informação para deduzir quais quadrados são seguros.")
    input("\nPressione Enter para voltar ao menu...")
    iniciarJogo()

def setTable():
    global field
    field = []

    for i in range(size):
        field.append([])
        for j in range(size):
            field[i].append(default)

def showTable():
    os.system("cls")

    for i in range(size):
        print(f"   {i+1}", end="")
    print("\n")

    for i in range(size):
        print(f"{i+1}", end="")
        for j in range(size):
            print(f" {field[i][j]} ", end="")
        print("\n")

def setBomb():
    global mine 
    mine = [] 
        
    for i in range(size):
        mine.append([])
        for j in range(size):
            mine[i].append(empty)

    for i in range(size):
        while True:
            x = random.randint(0, size-1)        
            y = random.randint(0, size-1)

            if mine[x][y] != bomb:
                mine[x][y] = bomb
                break

def showBombs(x, y, nome, hora_inicial):
    os.system("cls")

    for i in range(size):
        print(f"   {i+1}", end="")
    print("\n")

    for i in range(size):
        print(f"{i+1}", end="")
        for j in range(size):
            print(f" {mine[i][j]} ", end="")
        print("\n")
    
    print(f"Bomb! Você perdeu.")
    print(f"Você inseriu linha {x+1} coluna {y+1}")

    time.sleep(2)

    endGame(nome, hora_inicial)
    
def inputUser(nome, hora_inicial):
    while True:
        showTable()
        x = (int(input(f"Insira a linha que você deseja testar: ")) - 1)
        y = (int(input(f"Insira a coluna que você deseja testar: ")) - 1)
        bombTest(x, y, nome, hora_inicial)

def bombTest(x, y, nome, hora_inicial):
    global score

    if mine[x][y] == bomb:
        showBombs(x, y, nome, hora_inicial)
    else:
        score += 1
        bombsAround(x, y)

def bombsAround(x, y):
    x = int(x)
    y = int(y)

    bombsCount = 0

    for lineNumber in range(-1, 2):
        for columnNumber in range(-1, 2):
            if 0 <= x + lineNumber < size and 0 <= y + columnNumber < size:
                if mine[x + lineNumber][y + columnNumber] == bomb:
                    bombsCount += 1
                
    if bombsCount > 0:
        field[x][y] = bombsCount
    else:
        field[x][y] = empty

def endGame(nome, hora_inicial):
    hora_final = time.time()
    registerRank(nome, hora_inicial, hora_final)
    opcao = input("Você deseja jogar novamente? (S/N) ").upper()

    if opcao == "N":
        print(f"Obrigado {nome} pela tentativa.")
        print(f"Volte sempre!")
        time.sleep(3.5)
        iniciarJogo()
    elif opcao == "S":
        nome, hora_inicial = gameStart()  # Inicia o jogo e captura nome e hora inicial
        setTable()
        setBomb()
        inputUser(nome, hora_inicial)  # Passa nome e hora inicial para a função que gerencia as jogadas
    else:
        print("Por favor, insira apenas 'S' ou 'N'")
        endGame(nome, hora_inicial)

iniciarJogo()
