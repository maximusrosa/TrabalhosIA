import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Carregar o conjunto de dados MNIST
mnist = keras.datasets.mnist
#Carrega duas tuplas, representando os dados de treinamento e de teste.
#Cada tupla tem as imagens e os respectivos rótulos
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
num_classes = 10

plt.figure(figsize=(20, 4))

for i in range(num_classes):
    # treino
    ax = plt.subplot(2, num_classes, i + 1)
    plt.imshow(train_images[i])
    plt.title(f"treino, y={train_labels[i]}")
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # teste
    ax = plt.subplot(2, num_classes, i + 1 + num_classes)
    plt.imshow(test_images[i])
    plt.title(f"teste, y={test_labels[i]}")
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
plt.show()

# Converter para codificação one-hot dos labels
# Classe1 = [1, 0, 0,...]; Classe2 = [0, 1, 0,...]
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes=num_classes)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=num_classes)


#Não é necessário se utilizar como função de custo esparse_categorical_cross_entropy

# Crie o modelo de rede neural convolucional simples
def get_mnist_network():
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
        tf.keras.layers.Conv2D(num_filtros, (tam_filtro, tam_filtro), strides=(x_stride, y_stride), activation='relu',
                               input_shape=(32, 32, 3)),
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
                  loss='categorical_crossentropy',  # pode ser substituída pela esparse_categorical_cross_entropy
                  metrics=['accuracy'])

    model.summary()

    return model
