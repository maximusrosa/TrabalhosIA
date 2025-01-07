from typing import Tuple
from ..othello.gamestate import GameState
from .minimax import minimax_move
from .evaluate import evaluate_custom  
import time
import logging

logging.basicConfig(level=logging.INFO)

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Decide a jogada no Othello utilizando poda alfa-beta com controle de tempo.
    
    :param state: estado atual do jogo (instância de GameState)
    :return: (int, int) coordenadas da jogada (x, y)
    """
    max_time = 5  # Limite de tempo em segundos
    start_time = time.time()
    best_move = None
    depth = 1

    # Iterative deepening para respeitar o limite de tempo
    while time.time() - start_time < max_time:
        try:
            logging.info(f"Iniciando busca com profundidade {depth}")
            best_move = minimax_move(state, depth, evaluate_custom)
            depth += 1
        except TimeoutError:
            logging.warning("Tempo excedido durante a busca.")
            break

    if best_move is None:
        logging.warning("Nenhuma jogada encontrada. Escolhendo movimento aleatório.")
        return random.choice(state.legal_moves())

    logging.info(f"Melhor movimento escolhido: {best_move}")
    return best_move
