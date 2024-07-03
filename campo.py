import random         # para gerar números aleatórios
import sys            # para encerrar o programa
import time           # para gerar paradas temporárias
import os             # para executar funções do sistema operacional

# Constantes
BOMB = "💣"
EMPTY = "⬛"
DEFAULT = "⬜"
TEMP_BOMB = "❌"
TEMP_FIELD = "🟥"

# Variáveis globais
field = []     # campo total
mine = []      # local das minas
size = 5       # tamanho do tabuleiro/número de bombas
score = 0
posicao = 0

def menu():
    os.system("cls")
    print("")
    print("Boas-vindas ao Campo Minado!")
    print("")
    print("01 - Iniciar o Jogo")
    print("02 - Ver Ranking")
    print("03 - Regras e Instruções")
    print("04 - Sair do Jogo")
    
    opcao = input("O que você deseja fazer? ")

    if opcao in ["1", "01"]:
        nome, hora_inicial = game_start()  # Inicia o jogo e captura nome e hora inicial
        set_table()
        set_bomb()
        input_user(nome, hora_inicial)  # Passa nome e hora inicial para a função que gerencia as jogadas
    elif opcao in ["2", "02"]:
        show_rank()
    elif opcao in ["3", "03"]:
        show_rules()
    elif opcao in ["4", "04"]:
        print("Obrigado por jogar. Volte sempre!")
        time.sleep(1)
        sys.exit()

def game_start():
    global score
    score = 0
    nome = input("Insira o seu nome: ")
    hora_inicial = time.time()
    return nome, hora_inicial

def register_rank(nome, hora_inicial, hora_final):
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

def show_rank():
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
        menu()
    else:
        print("Nenhum ranking disponível. Jogue uma partida primeiro.")
        time.sleep(2)
        menu()

#------------------------------------cleanCode- Natália-------------------------

def show_rules():
    os.system("cls")
    print("Regras e Instruções do Campo Minado:")
    print("1. O objetivo do jogo é revelar todos os quadrados que não contêm bombas.")
    print("2. Se você revelar um quadrado contendo uma bomba, você perde.")
    print("3. Se você revelar um quadrado vazio, ele mostrará o número de bombas adjacentes.")
    print("4. Use essa informação para deduzir quais quadrados são seguros.")
    input("\nPressione Enter para voltar ao menu...")
    menu()

def set_table():
    global field
    field = [[DEFAULT for _ in range(size)] for _ in range(size)]

def show_table():
    os.system("cls")

    header = "  " + " ".join(f"{i+1} " for i in range(size))
    print(header + "\n")

    for i in range(size):
        row = f"{i+1} " + " ".join(str(field[i][j]) for j in range(size))
        print(row)

def set_bomb():
    global mine
    mine = [[EMPTY for _ in range(size)] for _ in range(size)]
    
    bomb_positions = set()
    while len(bomb_positions) < size:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        bomb_positions.add((x, y))
    
    for x, y in bomb_positions:
        mine[x][y] = BOMB

"""
Melhorias realizadas Natália:

Nomes de variáveis e funções: Transferi nomes de variáveis para o inglês em padrão minúsculo com underline para melhor padronização

- show_rules() Modifiquei o sentido da nomenclatura da função iniciar jogo para: "menu" pois, já havia uma função chamada start_game com o propósito de realmente
iniciar a jogatina

- set_table() Modifiquei para torná-la mais legível ao eliminar o loop desnecessário e criar o campo de forma mais direta

- show_table() eliminei o uso repetido de prints e otimizei a formatação da saída

- set_bomb() inicializei a matriz de forma mais direta e usei um conjunto (bomb_positions) para rastrear as posições das bombas 
garantindo que cada posição seja única sem a necessidade de um loop grande

"""
#------------------------------------cleanCode- Leontino-------------------------

def show_bombs(x, y, player_name, start_time):
    """
    Exibe o campo com todas as bombas e informa ao jogador que ele perdeu.
    
    :param x: Posição x da célula onde a bomba foi encontrada
    :param y: Posição y da célula onde a bomba foi encontrada
    :param player_name: Nome do jogador
    :param start_time: Hora inicial do jogo
    """
    os.system("cls")
    
    # Exibe a linha superior com os números das colunas
    print("   ", end="")
    for i in range(size):
        print(f"   {i+1}", end="")
    print("\n")
    
    # Exibe o campo de minas com os números das linhas
    for i in range(size):
        print(f" {i+1} ", end="")
        for j in range(size):
            print(f" {mine[i][j]} ", end="")
        print("\n")
    
    print(f"Bomb! Você perdeu.")
    print(f"Você inseriu linha {x+1} coluna {y+1}")
    
    time.sleep(2)
    end_game(player_name, start_time)

def input_user(player_name, start_time):
    """
    Solicita ao usuário as coordenadas da célula que deseja revelar.
    
    :param player_name: Nome do jogador
    :param start_time: Hora inicial do jogo
    """
    while True:
        show_table()
        try:
            x = int(input("Insira a linha que você deseja testar: ")) - 1
            y = int(input("Insira a coluna que você deseja testar: ")) - 1
            if 0 <= x < size and 0 <= y < size:
                bomb_test(x, y, player_name, start_time)
            else:
                print(f"Por favor, insira valores entre 1 e {size}.")
        except ValueError:
            print("Por favor, insira valores válidos.")

def bomb_test(x, y, player_name, start_time):
    """
    Verifica se a célula escolhida pelo jogador contém uma bomba ou não.
    
    :param x: Posição x da célula
    :param y: Posição y da célula
    :param player_name: Nome do jogador
    :param start_time: Hora inicial do jogo
    """
    global score

    if mine[x][y] == BOMB:
        show_bombs(x, y, player_name, start_time)
    else:
        score += 1
        count_bombs_around(x, y)

def count_bombs_around(x, y):
    """
    Conta o número de bombas ao redor de uma célula e atualiza o campo de jogo.
    
    :param x: Posição x da célula
    :param y: Posição y da célula
    """
    bombs_count = 0

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and mine[nx][ny] == BOMB:
                bombs_count += 1

    field[x][y] = bombs_count if bombs_count > 0 else EMPTY

def end_game(player_name, start_time):
    """
    Finaliza o jogo, registra a pontuação e pergunta ao jogador se deseja jogar novamente.
    
    :param player_name: Nome do jogador
    :param start_time: Hora inicial do jogo
    """
    end_time = time.time()
    register_rank(player_name, start_time, end_time)
    option = input("Você deseja jogar novamente? (S/N) ").upper()

    if option == "N":
        print(f"Obrigado {player_name} pela tentativa.")
        print("Volte sempre!")
        time.sleep(3.5)
        menu()
    elif option == "S":
        player_name, start_time = game_start()
        set_table()
        set_bomb()
        input_user(player_name, start_time)
    else:
        print("Por favor, insira apenas 'S' ou 'N'")
        end_game(player_name, start_time)

"""
Melhorias realizadas Leontino:

Nomes de variáveis e funções: Usei nomes descritivos para variáveis e funções, seguindo boas práticas de programação.
Comentários: Adicionei comentários explicativos para cada função e bloco de código.
Validação de entrada: Adicionei validação de entrada na função input_user para garantir que as coordenadas estejam dentro dos limites do tabuleiro e que sejam valores válidos.
Estrutura de repetição: Usei um loop while True no end_game para garantir que o usuário insira uma opção válida (S ou N).
Condicionais simplificadas: Simplifiquei a lógica de atualização do campo com o operador ternário.
"""
# Inicia o jogo
menu()
