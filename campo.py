import random         # para gerar números aleatórios
import sys            # para encerrar o programa
import time           # para gerar paradas temporárias
import os             # para executar funções do sistema operacional

# Constantes
BOMB = "💣"
EMPTY = "⬛"
DEFAULT = "⬜"

# Variáveis globais
field = []     # campo total
mine = []      # local das minas
size = 5       # tamanho do tabuleiro/número de bombas
score = 0
position = 0

def clear_screen():
    os.system("cls")

def display_menu():
    clear_screen()
    print("\nBoas-vindas ao Campo Minado!\n")
    print("01 - Iniciar o Jogo")
    print("02 - Ver Ranking")
    print("03 - Regras e Instruções")
    print("04 - Sair do Jogo")
    
   
    option = input("O que você deseja fazer? ")

    if option in ["1", "01"]:
        player_name, start_time = start_game()  # Inicia o jogo e captura nome e hora inicial
        set_table()
        set_bomb()
        input_user(player_name, start_time)  # Passa nome e hora inicial para a função que gerencia as jogadas
    elif option in ["2", "02"]:
        display_ranking()
    elif option in ["3", "03"]:
        show_rules()
    elif option in ["4", "04"]:
        print("Obrigado por jogar. Volte sempre!")
        time.sleep(1)
        sys.exit()

def start_game():
    global score
    score = 0
    player_name = input("Insira o seu nome: ")
    start_time = time.time()
    return player_name, start_time

def register_score(player_name, start_time, end_time):
    global score
    duration = end_time - start_time

    players = []
    scores = []
    times = []

    if os.path.isfile("ranking.txt"):
        with open("ranking.txt", "r") as arq:
            data = arq.readlines()
    else:
        data = []

    for line in data:
        partes = line.strip().split(";")
        players.append(partes[0])
        scores.append(int(partes[1]))
        times.append(float(partes[2]))

    players.append(player_name)
    scores.append(score)
    times.append(duration)

    sorted_scores = sorted(zip(scores, times, players), key=lambda x: (-x[0], x[1]))
    scores2, times2, players2 = zip(*sorted_scores)

    with open("ranking.txt", "w") as arq:
        for player_name, score, time in zip(players2, scores2, times2):
            arq.write(f"{player_name};{score};{time:.3f}\n")

def display_ranking():
    global position
    position = 0

    if os.path.isfile("ranking.txt"):
        with open("ranking.txt", "r") as arq:
            data = arq.readlines()
        
        clear_screen()
        print("Ranking dos Jogadores:")
        print(f"{'Posição':>7} {'Nome':>20} {'Acertos':>10} {'Tempo (s)':>12}")

        for line in data:
            position += 1
            parts = line.strip().split(";")
            player_name, score, time = parts[0], int(parts[1]), float(parts[2])
            print(f"{position:>7} {player_name:>20} {score:>10} {time:>12.3f}")

        input("\nPressione Enter para voltar ao menu...")
        display_menu()
    else:
        print("Nenhum ranking disponível. Jogue uma partida primeiro.")
        time.sleep(2)
        display_menu()

"""
Melhorias realizadas Gustavo:

Nomes de variáveis e funções: Usei nomes descritivos para variáveis e funções, seguindo boas práticas de programação.
Comentários: Adicionei comentários explicativos em algumas funções, para facilitar a compreensão.
Padronização: atualizei os nomes da variáveis para minusculo separado por underline, conforme combinado com o resto do grupo e criando a correta padronização.
"""
#------------------------------------cleanCode- Natália-------------------------

def show_rules():
    clear_screen()
    print("Regras e Instruções do Campo Minado:")
    print("1. O objetivo do jogo é revelar todos os quadrados que não contêm bombas.")
    print("2. Se você revelar um quadrado contendo uma bomba, você perde.")
    print("3. Se você revelar um quadrado vazio, ele mostrará o número de bombas adjacentes.")
    print("4. Use essa informação para deduzir quais quadrados são seguros.")
    input("\nPressione Enter para voltar ao menu...")
    display_menu()

def set_table():
    global field
    field = [[DEFAULT for _ in range(size)] for _ in range(size)]

def show_table():
    clear_screen()

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
    clear_screen()
    
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
    register_score(player_name, start_time, end_time)
    option = input("Você deseja jogar novamente? (S/N) ").upper()

    if option == "N":
        print(f"Obrigado {player_name} pela tentativa.")
        print("Volte sempre!")
        time.sleep(3.5)
        display_menu()
    elif option == "S":
        player_name, start_time = start_game()
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
display_menu()
