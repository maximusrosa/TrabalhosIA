from typing import Iterable, Set, Tuple


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

        # Opcional (se não for útil, pode apagar esse atributo)
        if filhos is None:
            self.filhos = []
        else:
            self.filhos = filhos

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
    :return:
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


# Exemplo de uso
estado_inicial = "2_3541687"
print(sucessor(estado_inicial))


def expande(nodo: Nodo) -> Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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
