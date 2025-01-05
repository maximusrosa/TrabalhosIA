import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

MAX_DEPTH = 4

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    return minimax_move(state, MAX_DEPTH, evaluate_count)


def evaluate_count(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on the number of pieces of each color.
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """

    if state.is_terminal():
        if state.winner() == player:
            return 1  # Jogador venceu
        elif state.winner() is None:
            return 0  # Empate
        else:
            return -1  # Jogador Perdeu
    else:
        # Conta número de peças do jogador e do oponente
        board = state.get_board()
        player_count = board.num_pieces(player)
        opponent_count = board.num_pieces(Board.opponent(player))

        # Retorna a diferença entre as peças do jogador e do oponente
        return player_count - opponent_count
