import numpy as np
import torch

# implement your solution here
def get_grouped_mean():
  """
  Calcula a média da largura da sépala (sepal width) para cada espécie de Íris.
  """
  # O array 'iris_data' é carregado no escopo global deste script.
  # A 5ª coluna (índice 4) contém as espécies.
  # A 2ª coluna (índice 1) contém a largura da sépala.

  # 1. Encontrar as espécies únicas no conjunto de dados.
  #    A função np.unique retorna os nomes das espécies como bytestrings (ex: b'Iris-setosa').
  unique_species = np.unique(iris_data[:, 4])

  # 2. Inicializar uma lista para armazenar os resultados.
  grouped_results = []

  # 3. Iterar sobre cada espécie única para calcular a média.
  for species in unique_species:
    # Criar uma máscara booleana para selecionar apenas as linhas da espécie atual.
    mask = (iris_data[:, 4] == species)

    # Usar a máscara para extrair os valores de largura da sépala correspondentes.
    sepal_widths = iris_data[mask, 1]

    # Converter os valores de string para float para permitir o cálculo da média.
    sepal_widths_float = sepal_widths.astype(float)

    # Calcular a média dos valores.
    mean_value = np.mean(sepal_widths_float)

    # Decodificar o nome da espécie de bytestring para string.
    species_name = species.decode('utf-8')

    # Adicionar o resultado à lista no formato de saída esperado.
    # O formato [('espécie', valor)] é um pouco incomum, mas corresponde ao solicitado.
    grouped_results.append([(species_name, mean_value)])

  return grouped_results

# get data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_data = np.genfromtxt(url, delimiter=',', dtype=object)
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# calculate grouped mean and print
grouped_mean = get_grouped_mean()
for i in grouped_mean:
  # O loop imprimirá cada item da lista, que é outra lista contendo uma tupla.
  # Exemplo de impressão: [('Iris-setosa', 3.428)]
  print(i)