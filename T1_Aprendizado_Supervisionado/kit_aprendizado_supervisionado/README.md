# Trabalho de Regressão Linear e Redes Neurais

## Integrantes do Grupo

- **Artur Bernardo de Souza Santos** - Cartão de Matrícula: 334726 - Turma: A
- **Guilherme d'Ávila Pinheiro** - Cartão de Matrícula: 342346 - Turma: A
- **Maximus Borges da Rosa** - Cartão de Matrícula: 342337 - Turma: A

## Configurações da Regressão Linear

### Valores Iniciais

- **Intercepto (b):** 0
- **Inclinação (w):** 0
- **Taxa de Aprendizado (alpha):** 0.01
- **Número de Iterações (num_iterations):** 1000

### Resultados

- **Melhor Erro Quadrático Médio (EQM):** EQM final: 8.529433040552066

### Trabalho 1: Aprendizado Supervisionado

Coloque no seu Readme.md as características de cada dataset: quantas classes, quantas amostras
e qual o tamanho das imagens (altura x largura x canais de cor). Para cada dataset, faça pelo menos
5 testes com configurações diferentes e busque responder as seguintes questões

1. Investigue e reflita sobre os fatores que tornam os problemas de classificação de cada
   dataset mais ou menos complexos em cada dataset. Pense em uma relação de ordem de
   complexidade/dificuldade dos datasets (os datasets em ordem dos menos complexos/difíceis para os
   mais complexos/difíceis) e justifique a resposta. O mais importante nesta questão é a investigação e
   a reflexão e não o fato de a resposta estar precisa. O esperado nesta questão é a sequência de
   datasets em ordem de complexidade/dificuldade, seguido de uma hipótese de quais características
   do dataset influenciaram o seu ranking.

2. Qual a maior acurácia obtida em cada dataset e quais mudanças (em termos de
   configurações da estrutura da rede ou outros hiper-parâmetros) fizeram a performance melhorar (ou
   pior, caso tenha ocorrido piora em relação a alguma performance já avaliada).
   Observação: Vocês podem explorar aspectos extras (normalização, decaimento de taxa de
   aprendizagem, outras operações nas redes convolucionais, etc).

### Referências

https://brains.dev/2022/modelos-de-regressao-regressao-linear/

# Testes dos Datasets para CNN’s

## Cifar 10
- **num_classes** = 10
- **num_amostras** = 60.000
- **tam_imagens** = 32x32x3

### Parâmetros:
- **Camada convolucional:**
   - num_filtros = 32
   - dim_kernel = 3x3 (filtro)

- **Max Pooling:**
   - dim_pooling = 2x2

- **Neurônios na primeira camada do MLP**
   - neurons_in_layer = 64

### Config 0 (Default)
- Camada Convolucional (Relu)
- Max Pooling
- Flattening
- MLP

**Acurácia no conjunto de teste:** 10.00%  
**Tempo de treinamento:** 434.41 segundos

### Config 1
- Camada Convolucional (Relu)
- Camada Convolucional (Relu)
- Max Pooling
- Flattening
- MLP

**Acurácia no conjunto de teste:** 59.43%  
**Tempo de treinamento:** 426.24 segundos

### Config 2
- Camada Convolucional (Relu)
- Camada Convolucional (Relu)
- Camada Convolucional (Relu)
- Max Pooling
- Flattening
- MLP

**Acurácia no conjunto de teste:** 60.27%  
**Tempo de treinamento:** 304.34 segundos

### Config 3
- Camada Convolucional (Relu)
- Camada Convolucional (Relu)
- Max Pooling
- Camada Convolucional (Relu)
- Max Pooling
- Flattening
- MLP

**Acurácia no conjunto de teste:** 67.14%  
**Tempo de treinamento:** 302.56 segundos

### Config 4
- Camada Convolucional (Relu)
- Camada Convolucional (Relu)
- Max Pooling
- Camada Convolucional (Relu)
- Max Pooling
- Flattening
- MLP (neurons_fst_layer = 128)

**Acurácia no conjunto de teste:** 66.31%  
**Tempo de treinamento:** 328.73 segundos

### Config 5
- Camada Convolucional (Relu)
- Max Pooling
- Camada Convolucional (Relu)
- Max Pooling
- Camada Convolucional (Relu)
- Max Pooling
- Flattening
- MLP

**Acurácia no conjunto de teste:** 61.92%  
**Tempo de treinamento:** 152.43 segundos

### Config 6
- Camada Convolucional (Relu)
- Camada Convolucional (Relu) (num_filtros = 64)
- Max Pooling
- Camada Convolucional (Relu) (num_filtros = 128)
- Camada Convolucional (Relu) (num_filtros = 256)
- Max Pooling
- Flattening
- MLP

**Acurácia no conjunto de teste:** 70.41%  
**Tempo de treinamento:** 1378.01 segundos

### Hipóteses
- Houve um salto significativo de acurácia quando adicionamos uma segunda camada convolucional (Config 1) em sequência, isso indica que aprendeu mais padrões úteis.
- Adicionar mais uma terceira camada em sequência (Config 2) não obteve mais padrões úteis.
- Um max-pooling após essa segunda camada convolucional trouxe uma melhor acurácia, o que indica que as características em destaque reconhecidas nessa camada são mais relevantes. (Config 3).
- Como dobrar o número de neurônios de entrada da MLP não teve um impacto positivo (Config 4), isso indica que o entrave provavelmente não está na parte de classificação, e sim de “feature learning” o que seria coerente com o baixo número de classes.
- As características destacadas pelo max-pooling dentro dos padrões destacados reconhecidos pela primeira camada (Config 5) não são relevantes o suficiente para melhorar a acurácia.
- A tentativa de reconhecer cada vez mais padrões diferentes ao longo da rede não teve um efeito positivo significativo o suficiente, dado o custo computacional maior (Config 6). Isso pode indicar que os padrões mais relevantes estão localizados nas primeiras camadas.

---

## Cifar 100
- **num_classes** = 100
- **num_amostras** = 60.000
- **tam_imagens** = 32x32x3

### Parâmetros default:
- **Camada convolucional:**
   - num_filtros = 32
   - dim_kernel = 3x3 (filtro)

- **Max Pooling:**
   - dim_pooling = 2x2

- **Neurônios na primeira camada do MLP**
   - neurons_in_layer = 64

### Estrutura
- Camada Convolucional
- Max Pooling
- Flatten
- MLP

**Acurácia no conjunto de teste:** 1.00%  
**Tempo de treinamento:** 114.36 segundos

### Testes
Observamos que dobrar o número de filtros para 64 aumentou o tempo de treinamento e não trouxe melhora na acurácia (1%, em 227.81 segundos), isso indica que o dataset não é complexo, variado ou grande o suficiente para aproveitar o uso de mais filtros. Há uma saturação nos padrões e características úteis para a classificação deste dataset, podendo ainda fazer com que ocorra overfitting.

Depois adicionamos mais três camadas convolucionais sem max pooling entre elas, não houve melhora na acurácia (1%, em 337.78 segundos), isso ilustra que não utilizar o max pooling e adicionar muitas camadas convolucionais pode impedir que a rede neural consiga abstrair padrões de mais alto nível e ainda causar overfitting.

Na terceira configuração dobramos o número de neurônios na primeira camada totalmente conexa do MLP, passou de 64 para 128. Observamos uma melhora na acurácia sem um aumento tão grande no tempo de treinamento (14.98% em 198.06 segundos). Nesse caso, o aumento significativo pode indicar que a parte convolucional não está extraindo características suficientemente discriminativas e o MLP com mais neurônios está compensando esse problema, isso pode ser porque o dataset tem dados similares e é mais difícil de classificar, mas nesse caso deve estar conectado ao fato de termos apenas uma camada convolucional, o que é simples demais para esse dataset.

Isso é demonstrado quando mantemos os neurônios em 64 e adicionamos uma camada convolucional a mais, ganhamos uma melhora significativa (21.35% em 189.92 segundos). Adicionando a isso um max pooling e depois outra camada convolucional temos (27.37% em 181.04 segundos). Porém se utilizarmos um max pooling entre cada uma das três camadas convolucionais não temos melhora (23.03% em 103.73 segundos), o que indica que o feature map pode ter sido reduzido demais e padrões importantes foram perdidos.

Por último, aumentamos novamente o número de neurônios do MLP tendo uma melhora mais tênue como o esperado (30.61% em 194.86 segundos).

### Melhor configuração obtida:
- Camada Convolucional
- Camada Convolucional
- Max Pooling
- Camada Convolucional
- Flatten
- MLP (com 128 neurônios na primeira camada)

## MNIST
- **num_classes** = 10
- **num_amostras** = 70.000
- **tam_imagens** = 28x28x1

### Parâmetros Default:
- **Camada convolucional:**
    - num_filtros = 16
    - tam_filtro = 3x3

- **Max Pooling:**
    - tam_pooling = 2x2

- **Só uma camada de saída no MLP**

### Estrutura
- Camada Convolucional
- Max Pooling
- Flatten
- MLP

**Acurácia no conjunto de teste:** 97.36%  
**Tempo de treinamento:** 68.71 segundos

### Testes
Primeiro adicionamos uma segunda camada convolucional obtendo uma melhora significativa (98.05% em 67.99 segundos), depois adicionamos um max pooling entre as duas camadas obtendo uma melhora insignificante (98.18% em 50.42 segundos), o que demonstra que o dataset pode não ser complexo o suficiente para se beneficiar de uma abstração maior dos padrões identificados, mas notamos que nas configurações mais complexas o max pooling teve uma melhora um pouco mais significativa, então mantemos ele.

Em seguida fizemos a segunda camada convolucional ter o dobro de filtros, 32, para tentar capturar mais detalhes nas imagens, obtendo uma pequena melhora (98.54% em 57.23 segundos).

Depois adicionamos uma camada totalmente conexa ao MLP com 64 neurônios, obtendo uma melhora insignificante (98.59% em 64.87 segundos). Observando a acurácia nos dados de treinamento em relação aos dados de teste, suspeitamos um pouco de overfitting, então adicionamos Early Stopping com paciência 3, obtendo uma melhora (98.74% em 70.71 segundos).

Por último, dobramos a quantidade de neurônios na camada do MLP, ficando com 128 neurônios, e obtemos uma pequena melhora (98.88% em 64.27 segundos).

### Melhor configuração obtida:
- Camada Convolucional (16 filtros)
- Max Pooling
- Camada Convolucional (32 filtros)
- Max Pooling
- Flatten
- MLP (com 128 neurônios na primeira camada)

## FASHION_MNIST
- **num_classes** = 10
- **num_amostras** = 70.000
- **tam_imagens** = 28x28x1

### Parâmetros Default:
- **Camada convolucional:**
    - num_filtros = 16
    - tam_filtro = 3x3

- **Max Pooling:**
    - tam_pooling = 2x2

- **Só uma camada de saída no MLP**

### Estrutura
- Camada Convolucional
- Max Pooling
- Flatten
- MLP

**Acurácia no conjunto de teste:** 86.23%  
**Tempo de treinamento:** 63.32 segundos

### Testes
Primeiro mudamos a camada para 32 filtros obtendo uma melhora de (86.24% em 78.43 segundos), nesse caso aumentar o número de filtros pode ter permitido que a rede capture características mais complexas nas imagens.

Depois adicionamos uma camada a mais, ambas com 16 filtros, obtendo (87.50% em 75.61 segundos). Apesar de terem menos filtros, a camada adicional permite que a rede combine características capturadas na primeira camada e forme padrões mais complexos.

Em seguida deixamos ambas as camadas com 32 filtros, o que permite uma representação mais rica dos dados e resultou em uma precisão ligeiramente maior de (89.04% em 143.76 segundos).

Adicionar um Max Pooling entre as camadas piorou a acurácia (87.63% em 81.58 segundos), portanto a redução do feature map pode ter causado a perda de dados significativos e, nesse caso, a abstração das informações não trouxe uma melhora na acurácia possivelmente devido a um dataset mais simples.

Por último, fizemos a primeira camada com 16 filtros e a segunda com 32 e obtemos quase a mesma acurácia da configuração com duas camadas de 32 filtros em menos tempo (88.92% em 98.78 segundos), isso indica que os padrões identificados com 16 filtros na primeira camada já são suficientes, e que a maior quantidade de filtros é mais útil para captar padrões mais profundos na segunda camada.

### Melhor configuração obtida:
- Camada Convolucional (16 filtros)
- Max Pooling
- Camada Convolucional (32 filtros)
- Max Pooling
- Flatten
- MLP (Só com camada de saída)

---

## Dificuldade dos Datasets
De mais difícil para menos:

### Cifar 100
O dataset mais difícil foi o Cifar 100, provavelmente devido ao número grande de classes - que cria padrões mais diversos na imagem e também pode causar mais situações de classes similares e pode exigir dados de treino mais complexos - e por possuir imagens coloridas, os filtros não só devem aprender a detectar padrões dentro de cada canal individual (vermelho, verde e azul), mas também devem aprender a integrar essas informações.

### Cifar 10
Apesar de bem mais fácil que o Cifar 100, ainda apresentou dificuldades, possivelmente devido ao fato de utilizar imagens coloridas, com 3 canais de cor, o que adiciona uma certa complexidade ao dataset em relação aos outros.

### Fashion MNIST
Mais difícil que o MNIST por causa das imagens e classes mais complexas, mas talvez por ser preto e branco e ter imagens com um grupo de objetos com características comuns entre eles e diferenças mais simples do que entre itens diversos como nos datasets Cifar.

### MNIST
Foi o mais fácil devido à simplicidade, os dígitos preto e branco foram os tipos de dados com padrões mais simples, que não requerem uma maior abstração de características.