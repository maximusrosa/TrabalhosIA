import numpy as np

def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    total_error = np.mean((data[:, 1] - (w * data[:, 0] + b)) ** 2)
    return total_error

def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    N = len(data)
    b_gradient = -2 * np.sum(data[:, 1] - (w * data[:, 0] + b)) / N
    w_gradient = -2 * np.sum((data[:, 1] - (w * data[:, 0] + b)) * data[:, 0]) / N
    new_b = b - alpha * b_gradient
    new_w = w - alpha * w_gradient
    return new_b, new_w

def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    b_values, w_values = [b], [w]
    for _ in range(num_iterations):
        b, w = step_gradient(b, w, data, alpha)
        b_values.append(b)
        w_values.append(w)
    return b_values, w_values
