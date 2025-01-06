import math
import random
from typing import Tuple

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # Estado do jogo
        self.parent = parent  # Nó pai
        self.children = []  # Nós filhos
        self.visits = 0  # Contagem de visitas
        self.wins = 0  # Contagem de vitórias

    def is_fully_expanded(self):
        """Verifica se todos os filhos possíveis foram expandidos."""
        return len(self.children) == len(self.state.get_valid_actions())

    def get_best_child(self, exploration_weight=1.0):
        """Retorna o melhor filho com base na fórmula UCB1."""
        return max(
            self.children,
            key=lambda child: child.wins / child.visits +
            exploration_weight * math.sqrt(math.log(self.visits) / (1 + child.visits))
        )

    def expand(self):
        """Expande a árvore gerando um novo filho com um estado ainda não explorado."""
        actions = self.state.get_valid_actions()
        for action in actions:
            # Verifica se o estado resultante da ação já foi expandido
            if not any(child.state == self.state.result(action) for child in self.children):
                new_state = self.state.result(action)
                child_node = Node(new_state, parent=self)
                self.children.append(child_node)
                return child_node
        return None


def simulate(state):
    """Simula uma partida aleatória a partir do estado atual até o estado terminal."""
    current_state = state
    while not current_state.is_terminal():
        actions = current_state.get_valid_actions()
        action = random.choice(actions)  # Escolhe uma ação aleatória
        current_state = current_state.result(action)
    return current_state.get_result()  # Retorna o vencedor do estado terminal


def backpropagate(node, result):
    """Retropropaga o resultado da simulação até a raiz da árvore."""
    while node:
        node.visits += 1
        if node.state.get_current_player() == result:
            node.wins += 1
        node = node.parent


def mcts(root_state, itermax=1000, exploration_weight=1.0):
    """
    Executa o algoritmo MCTS para selecionar a melhor jogada.
    
    :param root_state: O estado inicial do jogo.
    :param itermax: Número máximo de iterações.
    :param exploration_weight: Peso para a exploração na fórmula UCB1.
    :return: A melhor ação identificada pelo MCTS.
    """
    root = Node(root_state)

    for _ in range(itermax):
        node = root

        # 1. Seleção
        while not node.state.is_terminal() and node.is_fully_expanded():
            node = node.get_best_child(exploration_weight)

        # 2. Expansão
        if not node.state.is_terminal():
            node = node.expand()

        # 3. Simulação
        result = simulate(node.state)

        # 4. Retropropagação
        backpropagate(node, result)

    # Retorna a melhor ação do nó raiz
    best_child = root.get_best_child(0)  # Sem peso de exploração
    return best_child.state.get_last_action()


def make_move(state) -> Tuple[int, int]:
    """
    Decide a melhor jogada usando MCTS.

    :param state: O estado atual do jogo.
    :return: A ação (x, y) escolhida pelo MCTS.
    """
    return mcts(state, itermax=1000)
