import math
import random
from typing import Tuple, Optional
from ..othello.gamestate import GameState


class Node:
    def __init__(self, state: GameState, parent: Optional['Node'] = None, move: Optional[Tuple[int, int]] = None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.value = 0.0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.legal_moves())

    def best_child(self, exploration_weight: float = 1.0):
        return max(
            self.children,
            key=lambda child: (child.value / (child.visits + 1)) +
            exploration_weight * math.sqrt(math.log(self.visits + 1) / (child.visits + 1))
        )

    def expand(self):
        untried_moves = self.state.legal_moves() - {child.move for child in self.children}
        if untried_moves:
            move = random.choice(list(untried_moves))
            next_state = self.state.next_state(move)
            child_node = Node(next_state, parent=self, move=move)
            self.children.append(child_node)
            return child_node
        return None


def mcts(state: GameState, simulations: int = 1000) -> Tuple[int, int]:
    root = Node(state)

    for _ in range(simulations):
        # 1. Selection
        node = root
        while not node.state.is_terminal() and node.is_fully_expanded():
            node = node.best_child()

        # 2. Expansion
        if not node.state.is_terminal():
            node = node.expand()

        # 3. Simulation
        current_state = node.state
        while not current_state.is_terminal():
            legal_moves = list(current_state.legal_moves())
            if not legal_moves:
                break
            move = random.choice(legal_moves)
            current_state = current_state.next_state(move)

        # 4. Backpropagation
        result = current_state.winner()
        while node is not None:
            node.visits += 1
            if result == node.state.player:
                node.value += 1  # Win
            elif result is not None and result != node.state.player:
                node.value -= 1  # Loss
            node = node.parent

    # Return the move associated with the best child of the root
    return root.best_child(exploration_weight=0).move


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns a move for the given game state using MCTS.
    """
    if not state.legal_moves():
        raise ValueError("No legal moves available")
    print(f"Legal moves: {state.legal_moves()}")
    return mcts(state, simulations=500)
