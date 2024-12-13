from typing import Iterable, Set, Tuple
import heapq

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    def __init__(self, estado: str, pai: 'Nodo', acao: str, custo: int, filhos: list['Nodo'] = None):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """

        self.pai = pai
        self.estado = estado
        self.acao = acao
        self.custo = custo
        self.filhos = []

    def __lt__(self, other):
        return (self.custo + self.h) < (other.custo + other.h)

    def __eq__(self, other: 'Nodo') -> bool:
        """
        Verifica se dois nodos são iguais
        :param other: Nodo
        :return: bool
        """

        return (self.estado == other.estado and
                self.pai == other.pai and
                self.acao == other.acao and
                self.custo == other.custo)

    def __hash__(self) -> int:
        """
        Retorna o hash do objeto
        :return: int
        """
        return hash((self.estado, self.pai, self.acao, self.custo))

def sucessor(estado: str) -> Set[Tuple[str, str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return: Set[Tuple[str, str]]
    """

    # Movimentos possíveis associados ao deslocamento da peça vazia
    movimentos = {
        'esquerda': -1,
        'direita': 1,
        'acima': -3,
        'abaixo': 3
    }

    posicao_vazia = estado.index('_')

    # Conjuntos são úteis, pois evitam a repetição de estados
    resultado = set()

    def movimento_valido(acao, posicao_vazia):
        return (acao == 'esquerda' and posicao_vazia % 3 != 0) or \
            (acao == 'direita' and posicao_vazia % 3 != 2) or \
            (acao == 'acima' and posicao_vazia > 2) or \
            (acao == 'abaixo' and posicao_vazia < 6)

    for acao, deslocamento in movimentos.items():
        if movimento_valido(acao, posicao_vazia):
            nova_posicao = posicao_vazia + deslocamento

            # Conversão de string para lista para facilitar a manipulação
            estado_lista = list(estado)

            estado_lista[posicao_vazia], estado_lista[nova_posicao] = estado_lista[nova_posicao], estado_lista[
                posicao_vazia]

            novo_estado = ''.join(estado_lista)

            resultado.add((acao, novo_estado))

    return resultado

def expande(nodo: Nodo) -> Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return: Node iterable
    """
    sucessores = sucessor(nodo.estado)
    novos_nodos = set()

    for acao, novo_estado in sucessores:
        novo_nodo = Nodo(
            estado=novo_estado,
            pai=nodo,
            acao=acao,
            custo=nodo.custo + 1
        )
        nodo.filhos.append(novo_nodo)
        novos_nodos.add(novo_nodo)

    return novos_nodos

def printArvore(nodo: Nodo, nivel: int = 0):
    """
    Função para imprimir de estados para testes.
    :param nodo: Nodo
    :param nivel: int
    :return: None
    """
    if nodo is not None:
        print('  ' * nivel, nivel, nodo.estado, nodo.acao)
        for filho in nodo.filhos:
            printArvore(filho, nivel + 1)

def geraArvore(estado_inicial, niveis: int = 2):
    """
    Função para gerar árvore de estados para testes.
    :param nodo: Nodo
    :param nivel: int
    :return: None
    """
    nodoRaiz = Nodo(estado_inicial, None, None, 0)
    lista_nodos = expande(nodoRaiz)
    for i in range(niveis):
        for nodo in lista_nodos:
            novos_nodos = expande(nodo)
        lista_nodos = novos_nodos
    printArvore(nodoRaiz)

def hamming_dist(estado: str):
    """
    Função para calcular a distância de Hamming de um estado para o objetivo.
    :param estado:
    :return: int
    """
    objetivo = "12345678_"
    i = 0 
    h = 0
    for charEstado in estado:
        if charEstado != objetivo[i]:
            h += 1
        i += 1
    return h

def manhattan_dist(estado: str):
    """
    Função para calcular a distância de Hamming de um estado para o objetivo.
    :param estado:
    :return: int
    """
    objetivo = "12345678_"
    h = 0
    thisH = 0
    for charPos in range(8):
        charObjetivo = objetivo[charPos]
        dist = abs(estado.find(charObjetivo) - charPos)
        if dist != 0:
            thisH = dist % 3 + dist // 3
        else:
            thisH = 0
        h += thisH
        #print("'" + charObjetivo + "' tinha " + str(dist) + " de distância do objetivo. H: " + str(thisH) + '\n')
    return h

def reconstrucao_caminho(nodo):
    """
    Função para reconstruir o caminho percorrido do nodo raiz até o nodo atual.
    :param nodo: Nodo
    :return: str list (lista de ações)
    """
    caminho = []
    # Adiciona a ação do nodo atual e sobe para o seu pai até chegar na raiz.
    # Essa lista revertida representa um caminho até a solução objetivo.
    while nodo.pai is not None:
        caminho.append(nodo.acao)
        nodo = nodo.pai
    return list(reversed(caminho))

def busca_grafo(estado_inicial, heuristica):
    """
    Função para construir a árvore de busca e encontrar o caminho até o objetivo.
    :param estad_inicial: str
    :param heuristica: function
    :return: str list 
    (lista de ações que levam ao objetivo se existe, Null se não existe e Lista vazia se estado_inicial = objetivo.)
    """
    # Verifica se estado inicial já é o estado objetivo.
    if estado_inicial == "12345678_":
        return []

    # Cria nodo raiz
    nodo_inicial = Nodo(estado_inicial, None, None, 0, heuristica(estado_inicial))
    fronteira = []
    # O menor item (menor valor f = g + h) é sempre o primeiro da lista.
    heapq.heappush(fronteira, nodo_inicial)
    explorados = set()

    while fronteira:
        # Nodo da fronteira é movido para nodo_atual.
        nodo_atual = heapq.heappop(fronteira)

        # Verifica se o estado do nodo atual é o objetivo.
        # Se for retrocede ao longo do caminho percorrido e retorna a lista de ações para a solução objetivo.
        if nodo_atual.estado == "12345678_":
            return reconstrucao_caminho(nodo_atual)
        
        # Se o estado do nodo atual não é o objetivo, adiciona o estado do nodo atual ao conjunto de explorados.
        if nodo_atual.estado not in explorados:
            explorados.add(nodo_atual.estado)
            # Em seguida, expande o nodo atual e adiciona seus filhos à fronteira.
            for filho in expande(nodo_atual):
                # O heapq mantém a fronteira ordenada pelo valor de f = g + h.
                if filho.estado not in explorados:
                    filho.h = heuristica(filho.estado)
                    heapq.heappush(fronteira, filho)

    # Se a fronteira está vazia e nenhuma solução foi encontrada, retorna None.
    return None

def astar_hamming(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e retorna uma lista de ações que leva do estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return: str list
    """
    return busca_grafo(estado, hamming_dist)


def astar_manhattan(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e retorna uma lista de ações que leva do estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return: str list
    """
    return busca_grafo(estado, manhattan_dist)


#opcional,extra
def bfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


#opcional,extra
def dfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


#opcional,extra
def astar_new_heuristic(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

# Exemplo de uso
estado_inicial = "2_3541687"
#h = manhatam_dist(estado_inicial)
#print(h)
#print("Estado Inicial: " + estado_inicial)
#geraArvore(estado_inicial, 3)

# Exemplo de uso
estado_inicial = "2_3541687"
print("A* com Hamming:", astar_hamming(estado_inicial))
print("A* com Manhattan:", astar_manhattan(estado_inicial))