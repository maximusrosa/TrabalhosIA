import time
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Carregar o conjunto de dados CIFAR-100
cifar100 = keras.datasets.cifar100
#Carrega duas tuplas, representando os dados de treinamento e de teste.
#Cada tupla tem as imagens e os respectivos rótulos
(train_images, train_labels), (test_images, test_labels) = cifar100.load_data()
num_classes = 100

# Defina as classes do CIFAR-100
'''class_names = [
    "Castor", "Golfinho", "Lontra", "Foca", "Baleia",
    "Peixe de aquário", "Linguado", "Arraia", "Tubarão", "Truta",
    "Orquídeas", "Papoulas", "Rosas", "Girassóis", "Tulipas",
    "Garrafas", "Tigelas", "Latas", "Copos", "Pratos",
    "Maçãs", "Cogumelos", "Laranjas", "Peras", "Pimentões",
    "Relógio", "Teclado de computador", "Lâmpada", "Telefone", "Televisão",
    "Cama", "Cadeira", "Sofá", "Mesa", "Guarda-roupa",
    "Abelha", "Besouro", "Borboleta", "Lagarta", "Barata",
    "Urso", "Leopardo", "Leão", "Tigre", "Lobo",
    "Ponte", "Castelo", "Casa", "Estrada", "Arranha-céu",
    "Nuvem", "Floresta", "Montanha", "Planície", "Mar",
    "Camelo", "Gado", "Chimpanzé", "Elefante", "Canguru",
    "Raposa", "Porco-espinho", "Gambá", "Guaxinim", "Cangambá",
    "Caranguejo", "Lagosta", "Caracol", "Aranha", "Verme",
    "Bebê", "Menino", "Menina", "Homem", "Mulher",
    "Crocodilo", "Dinossauro", "Lagarto", "Cobra", "Tartaruga",
    "Hamster", "Rato", "Coelho", "Musaranho", "Esquilo",
    "Bordo", "Carvalho", "Palmeira", "Pinho", "Salgueiro",
    "Bicicleta", "Ônibus", "Motocicleta", "Caminhonete", "Trem",
    "Cortador de grama", "Foguete", "Bonde", "Tanque", "Trator"
]'''

# Crie um dicionário para mapear as classes para as imagens correspondentes
class_to_image = {}
for i in range(num_classes):
    index = (test_labels == i).nonzero()[0][0]  # Encontre o primeiro índice da classe
    class_to_image[i] = test_images[index]

# Mostre uma imagem de cada classe
plt.figure(figsize=(20, 20))
for i in range(num_classes):  # Display all 100 classes
    plt.subplot(10, 10, i + 1)
    plt.xticks([])  # Remove x-axis labels
    plt.yticks([])  # Remove y-axis labels
    plt.imshow(class_to_image[i])
    #plt.xlabel(class_names[i])

plt.tight_layout()
plt.show()

# Converter para codificação one-hot dos labels
# Classe1 = [1, 0, 0,...]; Classe2 = [0, 1, 0,...]
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes=num_classes)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=num_classes)


#Não é necessário se utilizar como função de custo esparse_categorical_cross_entropy

# Crie o modelo de rede neural convolucional simples
def get_cifar100_network():
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
        tf.keras.layers.Dense(128, activation='relu'),
        # Camada com 10 neurônios de saída representativos das classes.
        tf.keras.layers.Dense(num_classes, activation='softmax')  # 10 classes de saída
    ])

    # Compile o modelo
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',#pode ser substituída pela esparse_categorical_cross_entropy
                  metrics=['accuracy'])

    model.summary()

    return model

# Treine o modelo
start_time = time.time()
model = get_cifar100_network()
model.fit(train_images, train_labels, epochs=10)
end_time = time.time()

training_time = end_time - start_time

# Avalie o modelo no conjunto de teste
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f'Acurácia no conjunto de teste: {test_accuracy * 100:.2f}%')
print(f'Tempo de treinamento: {training_time:.2f} segundos')