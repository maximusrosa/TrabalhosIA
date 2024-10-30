import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Carregar o conjunto de dados CIFAR-10
cifar10 = keras.datasets.cifar10
#Carrega duas tuplas, representando os dados de treinamento e de teste.
#Cada tupla tem as imagens e os respectivos rótulos
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
num_classes = 10

# Defina as classes do CIFAR-10
class_names = ['Avião', 'Automóvel', 'Pássaro', 'Gato', 'Cervo',
               'Cachorro', 'Sapo', 'Cavalo', 'Navio', 'Caminhão']

# Crie um dicionário para mapear as classes para as imagens correspondentes
class_to_image = {}
for i in range(num_classes):
    index = (test_labels == i).nonzero()[0][0]  # Encontre o primeiro índice da classe
    class_to_image[i] = test_images[index]

# Mostre uma imagem de cada classe
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.xticks([])  # Remova os rótulos do eixo x
    plt.yticks([])  # Remova os rótulos do eixo y
    plt.imshow(class_to_image[i])
    plt.xlabel(class_names[i])

plt.tight_layout()
plt.show()

# Converter para codificação one-hot dos labels
# Classe1 = [1, 0, 0,...]; Classe2 = [0, 1, 0,...]
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes=num_classes)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=num_classes)


#Não é necessário se utilizar como função de custo esparse_categorical_cross_entropy

# Crie o modelo de rede neural convolucional simples
def get_cifar10_network():
    # Atributos
    # Camada convolucional:
    num_filtros = 32
    tam_filtro = 3
    x_stride = 1
    y_stride = 1

    # Max Pooling:
    tam_pooling = 2

    # Testar
    # - stride igual ao tamanho do filtro (sem overlap)
    # - stride maior que o tamanho do filtro (overlap)
    # - maior tamanho da "área" de pooling (menos informação)

    model = keras.Sequential([
        # Camada convolucional 32 filtros 3x3.
        # Podemos mudar quantidade de filtros, tamanho do filtro é geralmente 3x3, o "stride" pode ser aumentado para agilizar a execução.
        tf.keras.layers.Conv2D(num_filtros, (tam_filtro, tam_filtro), strides=(x_stride, y_stride), activation='relu', input_shape=(32, 32, 3)),
        #(32, 32, 3) porque as imagens são 32X32 e RGB, portanto, tendo 3 canais de cor

        # Max Pooling 2x2.
        # Podemos aumentar tamanho para agilizar execução, mas perdemos precisão.
        tf.keras.layers.MaxPooling2D((tam_pooling, tam_pooling)),

        # Transforma matriz de pesos em vetor.
        tf.keras.layers.Flatten(),

        # Camada de entrada com unção de ativação Relu.
        tf.keras.layers.Dense(64, activation='relu'),
        # Camada com 10 neurônios de saída representativos das classes.
        tf.keras.layers.Dense(num_classes, activation='softmax')  # 10 classes de saída
    ])

    # Compile o modelo
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',#pode ser substituída pela esparse_categorical_cross_entropy
                  metrics=['accuracy'])

    model.summary()

    return model