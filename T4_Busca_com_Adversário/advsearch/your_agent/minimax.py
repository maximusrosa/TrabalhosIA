import random
import logging
from typing import Tuple, Callable

logging.basicConfig(level=logging.INFO)

def max_value(state, player, alpha, beta, depth, max_depth, eval_func) -> float:
    if state.is_terminal() or (max_depth != -1 and depth == max_depth):
        score = eval_func(state, player)
        logging.debug(f"[MAX] Avaliando estado terminal ou limite: {score}")
        return score

    value = float("-inf")
    for move in state.legal_moves():
        next_state = state.next_state(move)
        value = max(value, min_value(next_state, player, alpha, beta, depth + 1, max_depth, eval_func))
        alpha = max(alpha, value)
        if alpha >= beta:
            logging.debug(f"[MAX] Poda aplicada (alpha={alpha}, beta={beta}, depth={depth})")
            break
    return value


def min_value(state, player, alpha, beta, depth, max_depth, eval_func) -> float:
    if state.is_terminal() or (max_depth != -1 and depth == max_depth):
        score = eval_func(state, player)
        logging.debug(f"[MIN] Avaliando estado terminal ou limite: {score}")
        return score

    value = float("inf")
    for move in state.legal_moves():
        next_state = state.next_state(move)
        value = min(value, max_value(next_state, player, alpha, beta, depth + 1, max_depth, eval_func))
        beta = min(beta, value)
        if beta <= alpha:
            logging.debug(f"[MIN] Poda aplicada (alpha={alpha}, beta={beta}, depth={depth})")
            break
    return value


def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    best_move = None
    best_value = float("-inf")
    alpha = float("-inf")
    beta = float("inf")
    player = state.player

    logging.info(f"Iniciando minimax para jogador {player} com profundidade máxima {max_depth}")

    legal_moves = state.legal_moves()
    if not legal_moves:
        logging.warning("Nenhum movimento válido encontrado. Retornando movimento aleatório.")
        return random.choice(state.legal_moves())

    for move in legal_moves:
        next_state = state.next_state(move)
        move_value = min_value(next_state, player, alpha, beta, 1, max_depth, eval_func)
        logging.debug(f"Movimento {move} avaliado com valor {move_value}")

        if move_value > best_value:
            best_value = move_value
            best_move = move

        alpha = max(alpha, best_value)

    logging.info(f"Melhor movimento encontrado: {best_move} com valor {best_value}")
    return best_move
