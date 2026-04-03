# Dever de casa - aula 5

import math

def analisar(a, b, k, p):
    c = math.log(a, b)
    epsilon = 1e-6

    print(f"\nlog_b(a) = {c:.4f}")

    if k < c - epsilon:
        print("Caso 1")
        print(f"T(n) = Θ(n^{c:.4f})")

    elif abs(k - c) <= epsilon:
        print("Caso 2")
        print(f"T(n) = Θ(n^{c:.4f} log^{p+1}(n))")

    else:
        print("Caso 3")
        print(f"T(n) = Θ(n^{k} log^{p}(n))")


def menu():
    print("\n=== ANALISADOR DE COMPLEXIDADE ===")
    print("1 - Merge Sort")
    print("2 - Multiplicação de Matrizes")
    print("3 - Recorrências do exercício")
    print("4 - Inserir manualmente")

    op = int(input("Escolha: "))

    if op == 1:
        analisar(2, 2, 1, 0)

    elif op == 2:
        analisar(8, 2, 2, 0)

    elif op == 3:
        print("\n(a) T(n) = 2T(n/4) + sqrt(n)")
        analisar(2, 4, 0.5, 0)

        print("\n(b) T(n) = 2T(n/4) + n")
        analisar(2, 4, 1, 0)

        print("\n(c) T(n) = 16T(n/4) + n^2")
        analisar(16, 4, 2, 0)

    elif op == 4:
        a = float(input("a: "))
        b = float(input("b: "))
        k = float(input("k: "))
        p = float(input("p: "))
        analisar(a, b, k, p)

menu()