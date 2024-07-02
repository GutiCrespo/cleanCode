import random         # para gerar números aleatórios
import sys            # para encerrar o programa
import time           # para gerar paradas timerárias
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
position = 0

def menu():
    os.system("cls")    
    print("")
    print("Boas-vindas ao Campo Minado!")
    print("")
    print("01 - Iniciar o Jogo")
    print("02 - Ver Ranking")
    print("03 - Regras e Instruções")
    print("04 - Sair do Jogo")
    
    option = input("O que você deseja fazer? ")

    if option == "1" or option == "01":
        name, start_time = gameStart()  
        setTable()
        setBomb()
        inputUser(name, start_time) 
    elif option == "2" or option == "02":
        showRank()
    elif option == "3" or option == "03":
        showRules()
    elif option == "4" or option == "04":
        print("Obrigado por jogar. Volte sempre!")
        time.sleep(1)
        sys.exit()

def gameStart():
    global score
    score = 0
    name = input("Insira o seu nome: ")
    start_time = time.time()
    return name, start_time

def registerRank(name, start_time, end_time):
    global score
    time = end_time - start_time

    players = []
    hits = []
    times = []

    if os.path.isfile("ranking.txt"):
        with open("ranking.txt", "r") as arq:
            datas = arq.readlines()
    else:
        datas = []

    for line in datas:
        parts = line.strip().split(";")
        players.append(parts[0])
        hits.append(int(parts[1]))
        times.append(float(parts[2]))

    players.append(name)
    hits.append(score)
    times.append(time)

    join = sorted(zip(hits, times, players), key=lambda x: (-x[0], x[1]))
    hits2, times2, players2 = zip(*join)

    with open("ranking.txt", "w") as arq:
        for player, hit, time in zip(players2, hits2, times2):
            arq.write(f"{player};{hit};{time:.3f}\n")

def showRank():
    global position
    position = 0

    if os.path.isfile("ranking.txt"):
        with open("ranking.txt", "r") as arq:
            datas = arq.readlines()
        
        os.system("cls")
        print("Ranking dos players:")
        print(f"{'Posição':>7} {'name':>20} {'hits':>10} {'time (s)':>12}")

        for line in datas:
            position += 1
            parts = line.strip().split(";")
            player, hit, time = parts[0], int(parts[1]), float(parts[2])
            print(f"{position:>7} {player:>20} {hit:>10} {time:>12.3f}")

        input("\nPressione Enter para voltar ao menu...")
        menu()
    else:
        print("Nenhum ranking disponível. Jogue uma partida primeiro.")
        time.sleep(2)
        menu()

def showRules():
    os.system("cls")
    print("Regras e Instruções do Campo Minado:")
    print("1. O objetivo do jogo é revelar todos os quadrados que não contêm bombas.")
    print("2. Se você revelar um quadrado contendo uma bomba, você perde.")
    print("3. Se você revelar um quadrado vazio, ele mostrará o número de bombas adjacentes.")
    print("4. Use essa informação para deduzir quais quadrados são seguros.")
    input("\nPressione Enter para voltar ao menu...")
    menu()

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

def showBombs(x, y, name, start_time):
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

    endGame(name, start_time)
    
def inputUser(name, start_time):
    while True:
        showTable()
        x = (int(input(f"Insira a linha que você deseja testar: ")) - 1)
        y = (int(input(f"Insira a coluna que você deseja testar: ")) - 1)
        bombTest(x, y, name, start_time)

def bombTest(x, y, name, start_time):
    global score

    if mine[x][y] == bomb:
        showBombs(x, y, name, start_time)
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

def endGame(name, start_time):
    end_time = time.time()
    registerRank(name, start_time, end_time)
    option = input("Você deseja jogar novamente? (S/N) ").upper()

    if option == "N":
        print(f"Obrigado {name} pela tentativa.")
        print(f"Volte sempre!")
        time.sleep(3.5)
        menu()
    elif option == "S":
        name, start_time = gameStart()  # Inicia o jogo e captura name e hora inicial
        setTable()
        setBomb()
        inputUser(name, start_time)  # Passa name e hora inicial para a função que gerencia as jogadas
    else:
        print("Por favor, insira apenas 'S' ou 'N'")
        endGame(name, start_time)

menu()
