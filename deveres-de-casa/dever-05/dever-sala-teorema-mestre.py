# Dever de sala - aula 5
import math

def analisar_teorema_mestre(a, b, k, p):
    # calcula log_b(a)
    c = math.log(a, b)

    print(f"\nlog_b(a) = {c:.4f}")
    print(f"Comparando f(n) = n^{k} log^{p}(n) com n^{c:.4f}\n")

    # margem de erro (para comparação de float)
    epsilon = 1e-6

    if k < c - epsilon:
        print("👉 Caso 1 do Teorema Mestre")
        print(f"T(n) = Θ(n^{c:.4f})")

    elif abs(k - c) <= epsilon:
        print("👉 Caso 2 do Teorema Mestre")
        print(f"T(n) = Θ(n^{c:.4f} * log^{p+1}(n))")

    else:  # k > c
        print("👉 Caso 3 do Teorema Mestre")
        print(f"T(n) = Θ(n^{k} * log^{p}(n))")


# ==========================
# INTERAÇÃO COM USUÁRIO
# ==========================

print("=== Analisador com Teorema Mestre ===")

a = float(input("Digite o valor de a (subproblemas): "))
b = float(input("Digite o valor de b (redução): "))
k = float(input("Digite o valor de k (expoente de n em f(n)): "))
p = float(input("Digite o valor de p (expoente do log): "))

analisar_teorema_mestre(a, b, k, p)