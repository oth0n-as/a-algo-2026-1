"""
Tic Tac Toe Player
"""

import math
import copy 

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

"""
A função player deve receber um estado do tabuleiro 
como entrada e retornar qual é o turno do jogador (X ou O).
No estado inicial do jogo, X recebe o primeiro movimento. 
Posteriormente, o jogador alterna com cada movimento adicional.
Qualquer valor de retorno é aceitável se o tabuleiro com a meta for 
fornecida como entrada (ou seja, o jogo já acabou).
"""
def player(board):
     
     x_count = sum(row.count(X) for row in board)
     o_count = sum(row.count(O) for row in board)
 
     # X começa o jogo; se X jogou mais vezes, é a vez de O
     return X if x_count == o_count else O

"""
A função actions deve retornar um conjunto de todas as ações 
possíveis que podem ser executadas em um determinado quadro.
Cada ação deve ser representada como uma tupla (i, j) onde i corresponde 
à linha do movimento (0, 1 ou 2) e j corresponde a qual
célula da linha corresponde ao movimento (também 0, 1 ou 2).
Os movimentos possíveis são quaisquer células do tabuleiro que ainda não tenham um X ou um O.
Qualquer valor de retorno é aceitável se uma placa de terminais for fornecida como entrada.
"""

def actions(board):

    possible_actions = set()
 
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
 
    return possible_actions

"""
A função result recebe um tabuleiro e uma ação como entrada e deve retornar um novo 
estado da placa, sem modificar a placa original.
Se a action não for uma ação válida para o tabuleiro, seu programa deverá gerar uma exceção.
O estado do tabuleiro retornado deve ser o tabuleiro que resultaria de pegar o 
tabuleiro de entrada original e permitir que ojogador de quem é o turno faça sua jogada na 
célula indicada pela ação de entrada.

É importante ressaltar que o tabuleiro original deve ser deixado sem modificações:
uma vez que o Minimax  acabará exigindo a consideração de muitos estados diferentes 
do tabuleiro durante seu processamento. Isso significa que simplesmente atualizar uma 
célula no quadro em si não é uma implementação correta da função de resultado. 
Você provavelmente desejará fazer uma cópia profunda do quadro antes de fazer qualquer alteração.
"""
def result(board, action):
     
    i, j = action
 
    if board[i][j] != EMPTY:
        raise ValueError(f"Ação inválida: a célula ({i}, {j}) já está ocupada.")
 
    # Cópia profunda para não modificar o tabuleiro original
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
 
    return new_board

"""
A função winner deve aceitar um tabuleiro como entrada e retornar o vencedor do tabuleiro, se houver.
Se o jogador X ganhou o jogo, sua função deve retornar X. Se o jogador O ganhou o jogo, sua função deve retornar O.

Pode-se ganhar o jogo com três de seus movimentos (marcações) seguidos horizontalmente, verticalmente ou diagonalmente.
Você pode presumir que haverá no máximo um vencedor (ou seja, nenhum tabuleiro jamais terá os dois jogadores com três em
linha, já que isso seria um estado de tabuleiro inválido).
Se não houver vencedor do jogo (seja porque o jogo está em andamento ou porque terminou empatado), a função deverá
retornar None.
"""
def winner(board):

    # Checa linhas e colunas
    for i in range(3):
        # Linha i
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # Coluna i
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
 
    # Checa diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
 
    return None

"""
A função terminal deve aceitar um tabuleiro como entrada e retornar um valor booleano 
indicando se o jogo acabou.

Se o jogo terminar, seja porque alguém ganhou o jogo ou porque todas as células foram 
preenchidas sem que ninguém ganhasse, a função deve retornar True.
Caso contrário, a função deve retornar False se o jogo ainda estiver em andamento.
"""
def terminal(board):
    
    # Jogo terminou se há um vencedor
    if winner(board) is not None:
        return True
 
    # Jogo terminou se não há células vazias (empate)
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return True
 
    return False

"""
A função utility deve receber um tabuleiro terminal como entrada e sua saída da 
utilidade do tabuleiro.

Se X ganhou o jogo, utility é 1. Se O ganhou o jogo, utility é -1. Se o jogo terminar empatado, 
a utilidade é 0.
Você pode assumir que utility só será chamado se um tabuleiro terminal for True.
"""
def utility(board):

     w = winner(board)
     if w == X:
        return 1
     elif w == O:
        return -1
     return 0

"""
A função minimax deve receber um tabuleiro como entrada e retornar o movimento ideal 
para o jogador se mover nesse tabuleiro.

O movimento devolvido deve ser a ação ideal (i, j) que é uma das ações permitidas no tabuleiro. 
Se vários movimentos forem igualmente ideais, qualquer um desses movimentos é aceitável.
Se o tabuleiro for terminal, a função minimax deverá retornar None.
"""
def minimax(board):

    if terminal(board):
        return None
 
    current_player = player(board)
 
    if current_player == X:
        # X quer maximizar
        _, best_action = max_value(board)
    else:
        # O quer minimizar
        _, best_action = min_value(board)
 
    return best_action

def max_value(board):
    """Retorna (utilidade, ação) para o jogador maximizador (X)."""
    if terminal(board):
        return utility(board), None
 
    v = -math.inf
    best_action = None
 
    for action in actions(board):
        min_v, _ = min_value(result(board, action))
        if min_v > v:
            v = min_v
            best_action = action
            if v == 1:  # Poda: não pode melhorar mais
                break
 
    return v, best_action
 
 
def min_value(board):
    """Retorna (utilidade, ação) para o jogador minimizador (O)."""
    if terminal(board):
        return utility(board), None
 
    v = math.inf
    best_action = None
 
    for action in actions(board):
        max_v, _ = max_value(result(board, action))
        if max_v < v:
            v = max_v
            best_action = action
            if v == -1:  # Poda: não pode melhorar mais
                break
 
    return v, best_action