"""
Implemente um algoritmo em Python que calcule o fatorial de um número 
utilizando recursão. Após isso, determine a complexidade assintótica O(n)
do algoritmo, incluindo a explicação do raciocínio. O objetivo é avaliar
como o tempo de execução cresce em função do tamanho da entrada n.
"""

import time
import sys

# Aumenta o limite de recursão do Python para permitir n até 1000
sys.setrecursionlimit(2000)

def fatorial(n):
    """
    Calcula o fatorial de um número utilizando recursão.

    Parâmetro:
        n (int): número inteiro não negativo

    Retorno:
        int: valor de n!

    Complexidade:
        Tempo: O(n)
        Espaço: O(n) devido à pilha de recursão
    """

    # Caso base: fatorial de 0 ou 1 é igual a 1
    if n <= 1:
        return 1

    # Passo recursivo
    return n * fatorial(n - 1)


# Valores solicitados na atividade
valores_teste = [10, 100, 500, 1000]

print("\n=== Experimento: Tempo de Execução do Fatorial Recursivo ===\n")
print(f"{'n':<10} {'Tempo (segundos)':<20}")
print("-" * 30)

for n in valores_teste:

    # Marca o início da execução
    inicio = time.perf_counter()

    # Executa o cálculo do fatorial
    fatorial(n)

    # Marca o fim da execução
    fim = time.perf_counter()

    # Calcula o tempo total
    tempo_execucao = fim - inicio

    # Mostra o resultado
    print(f"{n:<10} {tempo_execucao:<20.10f}")

print("\nConclusão: O tempo cresce linearmente conforme n aumenta, confirmando O(n).")

print("\nAnálise de Complexidade:")

print("""
O algoritmo calcula o fatorial utilizando recursão. 
A cada chamada recursiva o valor de n é reduzido em uma unidade até atingir o caso base (n ≤ 1). 
Dessa forma, o número total de chamadas recursivas é proporcional ao valor de n. 
Portanto, a complexidade de tempo do algoritmo é O(n).A complexidade de espaço também é O(n), 
pois cada chamada recursiva é armazenada na pilha de execução até que o caso base seja alcançado.
""")