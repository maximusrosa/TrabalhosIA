import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax com poda alfa-beta.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """
    if not state.legal_moves():
        # Nenhum movimento disponível; indica que a vez será passada
        return (-1, -1)

    return minimax_move(state, -1, utility)


def utility(state: GameState, player: str) -> float:
    """
    Calcula a utilidade de um estado terminal.
    :param state: Estado a ser avaliado.
    :param player: Jogador ('B' ou 'W').
    :return: Valor da utilidade (1, -1 ou 0).
    """
    if not state.is_terminal():
        raise ValueError("A função 'utility' só deve ser chamada para estados terminais.")

    winner = state.winner()
    if winner is None:
        return 0  # Empate

    # Vitória do jogador ou do oponente
    if winner == player:
        return 1 
    else:
        return -1
