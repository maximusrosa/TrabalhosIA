# Estrutura dos arquivos
# O diretório será zipado e conterá os seguintes arquivos:
# - Implementação completa
# - README.md com o relatório especificado

# Caminho onde os arquivos do projeto estão localizados
project_directory = "./T4_Busca_com_Adversario"
readme_content = """# Relatório do Projeto - Busca com Adversário

**Nomes e Matrículas:**
- **Artur Bernardo de Souza Santos** - Cartão de Matrícula: 334726 - Turma: A
- **Guilherme d'Ávila Pinheiro** - Cartão de Matrícula: 342346 - Turma: A
- **Maximus Borges da Rosa** - Cartão de Matrícula: 342337 - Turma: A

## Avaliação da Poda Alfa-Beta no Tic-Tac-Toe Misere

### Resultados
O agente que utiliza a poda alfa-beta demonstrou ser ótimo no jogo, alcançando os seguintes resultados:
- Sempre ganha ou empata, com 3 vitórias e 2 empates contra adversários aleatórios.
- Contra si mesmo, empatou todas as 5 partidas testadas.
- Contra os alunos perdeu com certa facilidade.

Conclusão: O agente não perdeu nenhuma partida no Tic-Tac-Toe Misere a não ser para alunos.

## Avaliação no Jogo Othello

### Heurística Customizada
A heurística projetada baseia-se em:
- **Valores Posicionais:** Um template de valores que avalia o impacto de cada posição no tabuleiro.
- **Mobilidade:** Diferença no número de movimentos válidos entre os jogadores.
- **Estabilidade:** Posições seguras que dificilmente podem ser revertidas pelo adversário.

#### Fontes Utilizadas:
A heurística foi adaptada a partir de conceitos encontrados [neste artigo](https://en.wikipedia.org/wiki/Reversi), com ajustes para o contexto do projeto e insights personalizados pelo grupo.

### Critério de Parada do Agente
Utilizamos o aprofundamento iterativo com limite de tempo (5 segundos por jogada). Isso permitiu melhor balanço entre tempo de execução e profundidade explorada.

### Resultados
Resultados das partidas entre diferentes agentes:

| Partida | Jogador B | Jogador W | Resultado |
|---------|-----------|-----------|-----------|
| 1       | Count     | Mask      | W venceu  |
| 2       | Mask      | Count     | B venceu  |
| 3       | Count     | Custom    | B venceu  |
| 4       | Custom    | Count     | B venceu  |
| 5       | Mask      | Custom    | B venceu  |
| 6       | Custom    | Mask      | W venceu  |

Conclusão: A heurística de **valor posicional** apresentou desempenho superior.

### Implementação Escolhida para o Torneio
A implementação baseada na heurística de valores posicionais (Mask) foi escolhida devido ao seu desempenho consistente e à capacidade de avaliar eficazmente o tabuleiro em diferentes situações.

### Extras
- **Técnicas Adicionais:** Implementamos melhorias na poda alfa-beta, otimizando cortes com base na profundidade e distribuindo os melhores movimentos para serem explorados primeiro.
- **Fontes Adicionais:**
  - Artigos sobre otimização de poda alfa-beta.
  - Estudos sobre estratégias de Othello.
  - ChatGPT e Gemini.

"""

