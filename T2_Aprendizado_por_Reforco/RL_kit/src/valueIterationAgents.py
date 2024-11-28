# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
        Inicializa o agente com o MDP, o fator de desconto e o número
        de iterações. Também executa o algoritmo de Iteração de Valor.

        Parâmetros:
        - mdp: um Markov Decision Process definido em mdp.py
        - discount: fator de desconto (gamma), controla o peso futuro
        - iterations: número de iterações do algoritmo de Iteração de Valor

        Inicializa um dicionário (Counter) para armazenar os valores dos estados.
        """
        self.mdp = mdp  # O MDP fornecido
        self.discount = discount  # Fator de desconto para valores futuros
        self.iterations = iterations  # Número de iterações do algoritmo
        self.values = util.Counter()  # Inicializa valores dos estados como 0

        # Executa Iteração de Valor para calcular valores ótimos
        for _ in range(self.iterations):
            new_values = util.Counter()  # Armazena os valores da iteração atual
            for state in self.mdp.getStates():  # Itera sobre todos os estados do MDP
                if self.mdp.isTerminal(state):  # Se o estado é terminal, continue
                    continue
                # Calcula o maior Q-value entre todas as ações possíveis
                action_values = [
                    self.computeQValueFromValues(state, action)
                    for action in self.mdp.getPossibleActions(state)
                ]
                # Define o novo valor como o máximo dos Q-values
                new_values[state] = max(action_values) if action_values else 0
            # Atualiza os valores para a próxima iteração
            self.values = new_values

    def getValue(self, state):
        """
        Retorna o valor de um estado armazenado em self.values.
S        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
        Calcula o valor Q(s, a) com base nos valores armazenados em self.values.

        Fórmula: Q(s, a) = Σ [P(s'|s,a) * (R(s,a,s') + γ * V(s'))]

        Parâmetros:
        - state: o estado atual
        - action: a ação a ser executada a partir do estado

        Retorna:
        - O valor Q para o par (estado, ação).
        """
        q_value = 0  # Inicializa o Q-value como 0
        for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, next_state)  # Recompensa para a transição
            # Soma ponderada da recompensa e valor do próximo estado
            q_value += prob * (reward + self.discount * self.values[next_state])
        return q_value

    def computeActionFromValues(self, state):
        """
        Retorna a melhor ação a ser executada em um estado com base
        nos valores armazenados em self.values.

        Parâmetro:
        - state: o estado atual

        Retorna:
        - A ação que maximiza o Q-value ou None se o estado for terminal.
        """
        if self.mdp.isTerminal(state):  # Se o estado é terminal, nenhuma ação é possível
            return None

        best_action = None
        best_value = float('-inf')  # Inicializa o melhor valor como menos infinito
        # Itera sobre todas as ações possíveis e calcula os Q-values
        for action in self.mdp.getPossibleActions(state):
            q_value = self.computeQValueFromValues(state, action)
            # Atualiza a melhor ação se o Q-value for maior que o atual
            if q_value > best_value:
                best_value = q_value
                best_action = action
        return best_action

    def getPolicy(self, state):
        """
        Retorna a política (melhor ação) para um estado específico.
        """
        return self.computeActionFromValues(state)

    def getAction(self, state):
        """
        Retorna a política no estado (nenhuma exploração é usada).
        """
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        """
        Retorna o Q-value calculado para um estado e uma ação.
        """
        return self.computeQValueFromValues(state, action)
