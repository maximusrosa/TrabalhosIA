# Trabalhos de Inteligência Artificial (INF01048)

Este repositório contém os códigos e materiais relacionados aos trabalhos práticos da disciplina de Inteligência Artificial (INF01048) da Universidade Federal do Rio Grande do Sul (UFRGS). Os projetos abrangem Aprendizado Supervisionado, Aprendizado por Reforço e Algoritmos de Busca, aplicados em problemas clássicos como regressão linear, redes neurais, o 8-puzzle e controle de agentes em ambientes simulados.

## Estrutura do Repositório

- `T1_Aprendizado_Supervisionado/`
    - `alegrete.py`: Implementação do algoritmo de regressão linear utilizando descida de gradiente.
    - `alegrete.ipynb`: Jupyter Notebook para carregar os dados de entrada e visualizar os resultados.
    - `Trabalho_redes_neurais.ipynb`: Configuração e testes de redes neurais usando TensorFlow/Keras em datasets como MNIST, Fashion MNIST, CIFAR-10 e CIFAR-100.
    - **Readme.md**: Explicações sobre os parâmetros escolhidos, análise dos datasets, resultados obtidos e observações.

- `T2_Reforco/`
    - `valueIterationAgents.py`: Implementação de iteração de valor para resolver MDPs.
    - `qlearningAgents.py`: Agentes Q-learning aplicados ao Gridworld, Crawler e Pacman.
    - `analysis.py`: Respostas às perguntas específicas do projeto.
    - **Readme.md**: Detalhes da implementação, parâmetros experimentais e análise dos resultados.

- `T3_8_Puzzle/`
    - `solucao.py`: Implementações das funções para resolver o 8-puzzle usando A* com heurísticas de Hamming e Manhattan.
    - `testa_solucao.py`: Script para testar se a implementação está correta.
    - **Readme.md**: Explicações sobre o uso das heurísticas, análise de desempenho e complexidade dos algoritmos.

- `T4_Busca_Com_Adversario/`
  - `minimax.py`: Implementação do algoritmo minimax com poda alfa-beta.
  - `othello_minimax_count.py`: Heurística de contagem para o jogo Othello.
  - `othello_minimax_mask.py`: Heurística de valor posicional para o jogo Othello.
  - `othello_minimax_custom.py`: Heurística customizada para o jogo Othello.
  - `tttm_minimax.py`: Implementação do minimax para o tic-tac-toe misere.
  - `tournament_agent.py`: Agente configurado para o torneio final do jogo Othello.
  - **Readme.md**: Explicação sobre as heurísticas desenvolvidas e estratégias para vencer o adversário.
  - 
## Pré-requisitos

- **Python 3.8** (versão compatível com Miniconda)
- **Bibliotecas adicionais**: Especifique e instale com `pip` ou `conda` conforme necessário, como `numpy`, `pandas`, `numba`, `tensorflow`.

## Instalação

Para clonar o repositório:
   ```bash
   git clone https://github.com/maximusrosa/TrabalhosIA
   cd TrabalhosIA
   ```

## Trabalhos

### T1: Aprendizado Supervisionado
Implementação de regressão linear com descida de gradiente e redes neurais utilizando TensorFlow/Keras. Inclui análise dos datasets, experimentação com configurações de rede, e comparação de desempenho.

- **Datasets**: MNIST, Fashion MNIST, CIFAR-10, CIFAR-100.
- **Análise**: Discussão sobre a complexidade dos datasets e estratégias para melhorar a performance.

### T2: Aprendizado por Reforço
Desenvolvimento de agentes de Aprendizado por Reforço (Value Iteration e Q-Learning) para resolver MDPs em ambientes simulados, como o Pacman.

- **Testes**: Autograder para verificar a corretude das soluções.
- **Desafios**: Ajustar parâmetros de ruído e desconto para políticas ótimas.

### T3: 8-Puzzle
Resolução do 8-puzzle utilizando o algoritmo A* com diferentes heurísticas.

- **Heurísticas**: Distância de Hamming e distância de Manhattan.
- **Análise de desempenho**: Expansão de nós, tempo decorrido e custo da solução.

### T4: Busca com Adversário
Implementação do algoritmo minimax com poda alfa-beta para jogos de tabuleiro como Othello e Tic-Tac-Toe.

- **Heurísticas**: Contagem de peças, valor posicional e customizada.
- **Torneio**: Estratégias para vencer o adversário em diferentes cenários.
- **Análise**: Discussão sobre a complexidade dos jogos e estratégias vencedoras.
- 

## Como Executar

- Para testar o autograder no Trabalho 2:
  ```bash
  python autograder.py
  ```
- Para executar a busca A* no Trabalho 3:
  ```bash
  python solucao.py
  ```

## Integrantes

- **Artur Bernardo de Souza Santos** - [@ArturBDev](https://github.com/ArturBDev)
- **Guilherme d'Ávila Pinheiro** - [@GuiDavilaP](https://github.com/GuiDavilaP)
- **Maximus Borges da Rosa** - [@maximusrosa](https://github.com/maximusrosa)

---
