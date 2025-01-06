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
    # Chama o minimax com poda alfa-beta passando a heurística customizada
    max_depth = 5  # Profundidade máxima para evitar estourar o tempo limite
    return minimax_move(state, max_depth, evaluate_custom)

def evaluate_custom(state: GameState, player: str) -> float:
    """
    Avalia um estado de Othello para o jogador dado usando uma heurística customizada.
    :param state: estado a ser avaliado (instância de GameState)
    :param player: jogador para quem o estado será avaliado ('B' ou 'W')
    :return: valor estimado do estado
    """
    # Heurística baseada em controle de quinas e estabilidade
    board = state.board
    opponent = 'B' if player == 'W' else 'W'
    
    # Pesos para diferentes aspectos do tabuleiro
    corner_weight = 50
    edge_weight = 10
    mobility_weight = 5
    stability_weight = 20

    # Quinas
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    corner_score = sum(
        corner_weight if board.tiles[y][x] == player else -corner_weight
        if board.tiles[y][x] == opponent else 0
        for x, y in corners
    )

    # Mobilidade (ações válidas)
    player_moves = len(state.get_valid_actions(player))
    opponent_moves = len(state.get_valid_actions(opponent))
    mobility_score = mobility_weight * (player_moves - opponent_moves)

    # Estabilidade (posições seguras no tabuleiro)
    # Essa parte pode ser expandida para calcular peças estáveis
    stability_score = stability_weight * (
        sum(row.count(player) for row in board.tiles) -
        sum(row.count(opponent) for row in board.tiles)
    )

    # Soma os componentes da heurística
    return corner_score + mobility_score + stability_score
