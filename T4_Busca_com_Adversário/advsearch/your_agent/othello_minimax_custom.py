import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Decide a jogada usando minimax com poda alfa-beta.
    :param state: estado atual do jogo (instância de GameState)
    :return: (int, int) tupla com as coordenadas x, y da jogada
    """
    max_depth = 5  # Profundidade máxima para evitar estourar o tempo limite
    return minimax_move(state, max_depth, evaluate_custom)

def evaluate_custom(state: GameState, player: str) -> float:
    """
    Avalia um estado de Othello para o jogador dado usando uma heurística customizada.
    :param state: estado a ser avaliado (instância de GameState)
    :param player: jogador para quem o estado será avaliado ('B' ou 'W')
    :return: valor estimado do estado
    """
    board = state.get_board()
    opponent = Board.opponent(player)

    # Verifica se o estado é terminal
    if state.is_terminal():
        winner = state.winner()
        if winner == player:
            return float('inf')  # Vitória para o jogador
        elif winner == opponent:
            return float('-inf')  # Vitória para o oponente
        else:
            return 0  # Empate

    # Pesos para diferentes aspectos do tabuleiro
    corner_weight = 50
    mobility_weight = 5
    stability_weight = 20

    # Quinas
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    corner_score = sum(
        corner_weight if board.tiles[y][x] == player else
        -corner_weight if board.tiles[y][x] == opponent else 0
        for x, y in corners
    )

    # Mobilidade
    player_moves = len(state.legal_moves()) if state.player == player else 0
    opponent_moves = (
        len(state.get_board().legal_moves(opponent)) if state.player == opponent else 0
    )
    mobility_score = mobility_weight * (player_moves - opponent_moves)

    # Estabilidade (peças seguras)
    stable_pieces_player = sum(row.count(player) for row in board.tiles)
    stable_pieces_opponent = sum(row.count(opponent) for row in board.tiles)
    stability_score = stability_weight * (stable_pieces_player - stable_pieces_opponent)

    # Soma os componentes da heurística
    return corner_score + mobility_score + stability_score

