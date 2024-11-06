import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import time

# Carregar o conjunto de dados MNIST
fashion_mnist = keras.datasets.fashion_mnist
#Carrega duas tuplas, representando os dados de treinamento e de teste.
#Cada tupla tem as imagens e os respectivos rótulos
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
num_classes = 10

'''
classes_roupas = [
    "Camiseta/Top",
    "Calça",
    "Pulôver",
    "Vestido",
    "Casaco",
    "Sandália",
    "Camisa",
    "Tênis",
    "Bolsa",
    "Bota"
]


plt.figure(figsize=(20, 4))

for i in range(num_classes):
    # treino
    ax = plt.subplot(2, num_classes, i + 1)
    plt.imshow(train_images[i])
    plt.title(f"Treinamento")
    plt.title(f"y={classes_roupas[train_labels[i]]}")
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # teste
    ax = plt.subplot(2, num_classes, i + 1 + num_classes)
    plt.imshow(test_images[i])
    plt.title(f"Teste")
    plt.title(f"y={classes_roupas[test_labels[i]]}")
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()

'''

# Converter para codificação one-hot dos labels
# Classe1 = [1, 0, 0,...]; Classe2 = [0, 1, 0,...]
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes=num_classes)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=num_classes)


#Não é necessário se utilizar como função de custo esparse_categorical_cross_entropy

# Crie o modelo de rede neural convolucional simples
def get_fashion_mnist_network():
    num_filtros = 16
    dim_filtro = 3

    # Max Pooling:
    dim_mat_max_pooling = 2

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(num_filtros, (dim_filtro, dim_filtro), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.Conv2D(2 * num_filtros, (dim_filtro, dim_filtro), activation='relu', input_shape=(26, 26, 1)),
        # 1 camada de convolução: 16 filtros 3x3, stride padrão (1,1), ativação relu
        tf.keras.layers.MaxPool2D((dim_mat_max_pooling, dim_mat_max_pooling), ),  # max pooling 2x2
        tf.keras.layers.Flatten(),  # achatar p/ se ajustar à MLP

        tf.keras.layers.Dense(num_classes, activation='softmax')  # 1 camada de saida com 10 neuronios
    ])

    model.compile('adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model


# Treine o modelo
start_time = time.time()
model = get_fashion_mnist_network()
model.fit(train_images, train_labels, epochs=10)
end_time = time.time()

training_time = end_time - start_time

# Avalie o modelo no conjunto de teste
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f'Acurácia no conjunto de teste: {test_accuracy * 100:.2f}%')
print(f'Tempo de treinamento: {training_time:.2f} segundos')
