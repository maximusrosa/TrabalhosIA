import random
from typing import Tuple, Callable
import logging
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

logging.basicConfig(level=logging.INFO)

# Profundidade máxima do Minimax
MAX_DEPTH = 4

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Calcula a melhor jogada para o estado atual usando Minimax com poda alfa-beta.
    
    :param state: Estado atual do jogo (instância de GameState).
    :return: Uma tupla (x, y) com as coordenadas do movimento escolhido.
    """
    if not state.legal_moves():
        logging.warning("Nenhum movimento disponível. Passando a vez.")
        return (-1, -1)  # Indica um movimento de passar a vez

    # Usa o algoritmo Minimax para determinar o melhor movimento
    return minimax_move(state, MAX_DEPTH, evaluate_count)


def evaluate_count(state: GameState, player: str) -> float:
    """
    Avalia um estado do jogo do ponto de vista do jogador especificado.
    Para estados terminais, retorna a diferença entre as peças do jogador e do oponente.
    Para estados não terminais, retorna a diferença de peças no tabuleiro.
    
    :param state: Estado a ser avaliado (instância de GameState).
    :param player: Jogador a avaliar o estado ('B' ou 'W').
    :return: Valor avaliado do estado.
    """
    board = state.get_board()

    # Conta as peças do jogador e do oponente
    player_count = board.num_pieces(player)
    opponent_count = board.num_pieces(Board.opponent(player))

    # Caso terminal: calcula pontuação com base na diferença de peças
    if state.is_terminal():
        if state.winner() == player:
            return player_count - opponent_count  # Vitória
        elif state.winner() is None:
            return 0  # Empate
        else:
            return player_count - opponent_count  # Derrota

    # Caso não terminal: retorna a diferença de peças
    return player_count - opponent_count



# Minimax com Poda Alfa-Beta
def max_value(state: GameState, player: str, alpha: float, beta: float, depth: int, max_depth: int, eval_func: Callable) -> float:
    """
    Função de maximização do Minimax com poda alfa-beta.
    """
    if state.is_terminal() or depth == max_depth:
        return eval_func(state, player)

    value = float("-inf")
    for move in state.legal_moves():
        next_state = state.next_state(move)
        value = max(value, min_value(next_state, player, alpha, beta, depth + 1, max_depth, eval_func))
        alpha = max(alpha, value)
        if alpha >= beta:
            break  # Poda
    return value


def min_value(state: GameState, player: str, alpha: float, beta: float, depth: int, max_depth: int, eval_func: Callable) -> float:
    """
    Função de minimização do Minimax com poda alfa-beta.
    """
    if state.is_terminal() or depth == max_depth:
        return eval_func(state, player)

    value = float("inf")
    for move in state.legal_moves():
        next_state = state.next_state(move)
        value = min(value, max_value(next_state, player, alpha, beta, depth + 1, max_depth, eval_func))
        beta = min(beta, value)
        if beta <= alpha:
            break  # Poda
    return value


def minimax_move(state: GameState, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Retorna o melhor movimento calculado pelo Minimax com poda alfa-beta.
    
    :param state: Estado atual do jogo (instância de GameState).
    :param max_depth: Profundidade máxima para o algoritmo Minimax.
    :param eval_func: Função de avaliação para calcular o valor de um estado.
    :return: Coordenadas (x, y) do melhor movimento.
    """
    best_move = None
    best_value = float("-inf")
    alpha = float("-inf")
    beta = float("inf")
    player = state.player

    logging.info(f"Calculando melhor movimento para jogador {player} com profundidade {max_depth}")

    for move in state.legal_moves():
        next_state = state.next_state(move)
        move_value = min_value(next_state, player, alpha, beta, 1, max_depth, eval_func)
        logging.debug(f"Movimento {move} avaliado em {move_value}")

        if move_value > best_value:
            best_value = move_value
            best_move = move
        alpha = max(alpha, best_value)

    if best_move is None:
        logging.warning("Nenhum movimento encontrado. Escolhendo movimento aleatório.")
        return random.choice(state.legal_moves())

    logging.info(f"Melhor movimento encontrado: {best_move} com valor {best_value}")
    return best_move
