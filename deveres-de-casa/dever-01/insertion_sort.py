# Implemente o algoritmo Insertion Sort O(n²)
# Dado um vetor, constrói um vetor ordenado, elemento por elemento

import time
import random

def insertion_sort(lista):

  for i in range (1, len(lista)):
    valor_atual = lista[i]
    j = i - 1 # Com quem eu vou comparar o i
    # Enquanto houver elementos à esquerda e o valor da esquerda for maior que o atual:
    while j >= 0 and lista[j] > valor_atual:
      lista[j + 1] = lista[j] # Move o maior para a frente
      j -= 1                  # Anda para trás

    # Agora que o espaço está aberto, coloca o valor na posição correta:
    lista[j + 1] = valor_atual

  return lista

tamanhos = [1000, 5000, 10000, 20000, 50000]

print(f"{'Tamanho':<10} | {'Insertion Sort':<15} | {'Sorted (Timsort)':<15}")
print("-" * 50)

for n in tamanhos:
  lista = [random.randint(0, 100000) for _ in range(n)]

  lista_copia = lista.copy()

  # 3. Medir Insertion Sort
  inicio = time.perf_counter()
  insertion_sort(lista)
  fim = time.perf_counter()
  tempo_insertion = fim - inicio

  # 4. Medir o sorted() nativo do Python
  inicio = time.perf_counter()
  sorted(lista_copia)
  fim = time.perf_counter()
  tempo_sorted = fim - inicio

  # 5. Imprimir os resultados
  print(f"{n:<10} | {tempo_insertion:<15.5f} | {tempo_sorted:<15.5f}")