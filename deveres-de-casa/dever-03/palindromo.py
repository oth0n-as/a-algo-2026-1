# Implemente o código recursivo para verificar se um array é palíndromo.

def is_array_palindrome(arr, inicio, fim):
  # Caso base
  if inicio >= fim:
    return True
  
  # Se os elementos forem diferentes
  if arr[inicio] != arr[fim]:
    return False
  
  # Chamada recursiva para o subarray interno
  return is_array_palindrome(arr, inicio + 1, fim - 1)

# Testando
arr = [1, 2, 3, 2, 1]
resultado = is_array_palindrome(arr, 0, len(arr) - 1)

if resultado:
    print("O array é palíndromo")
else:
    print("O array não é palíndromo")
  