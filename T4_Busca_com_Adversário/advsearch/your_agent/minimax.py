import random
from typing import Tuple, Callable

def max_value(
        state,
        player,
        alfa,
        beta,
        depth,
        max_depth,
        eval_func
) -> float:
    """
    Função de maximização com poda alfa-beta.
    Retorna o melhor valor avaliado para o estado atual.
    """
    if state.is_terminal() or (0 < max_depth <= depth):
        return eval_func(state, player)

    value = float("-inf")
    for move in state.legal_moves():
        next_state = state.next_state(move)
        value = max(value, min_value(next_state, player, alfa, beta, depth + 1, max_depth, eval_func))
        alfa = max(alfa, value)
        if alfa >= beta:
            break  # Poda
    return value

def min_value(
        state,
        player,
        alfa,
        beta,
        depth,
        max_depth,
        eval_func
) -> float:
    """
    Função de minimização com poda alfa-beta.
    Retorna o melhor valor avaliado para o estado atual.
    """
    if state.is_terminal() or (0 < max_depth <= depth):
        return eval_func(state, player)

    value = float("+inf")
    for move in state.legal_moves():
        next_state = state.next_state(move)
        value = min(value, max_value(next_state, player, alfa, beta, depth + 1, max_depth, eval_func))
        beta = min(beta, value)
        if beta <= alfa:
            break  # Poda
    return value

def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Retorna um movimento calculado pelo algoritmo Minimax com poda alfa-beta usando funções max_value e min_value.
    """
    # Se for o primeiro turno e o centro estiver disponível, priorize o movimento central
    if len(state.legal_moves()) == 9 and (1, 1) in state.legal_moves():
        return 1, 1

    best_move = None
    best_value = float('-inf')

    for move in state.legal_moves():
        next_state = state.next_state(move)
        move_value = min_value(next_state, state.player, float("-inf"), float("+inf"), 1, max_depth, eval_func)
        if move_value > best_value:
            best_value = move_value
            best_move = move

    return best_move
