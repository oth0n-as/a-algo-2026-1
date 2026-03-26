def F(n):
    """
    Função recursiva definida por:
    F(n) = 2F(n-1) + n²
    com caso base F(1) = 2
    """
    
    # Caso base
    if n == 1:
        return 2
    
    # Chamada recursiva
    return 2 * F(n-1) + n**2


# Programa principal
n = int(input("Digite um valor para n: "))

valor = F(n)

print("Resultado:", valor)