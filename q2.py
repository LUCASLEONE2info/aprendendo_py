def progressao_aritmetica(a1, n, r):
  """
  Função que calcula e imprime uma progressão aritmética.

  Args:
    a1: O 1° termo da PA.
    n: A quantidade de termos da PA.
    r: A razão da PA.
  """
  pa = []
  for i in range(n):
    an = a1 + i * r
    pa.append(an)
  print(f"Progressão Aritmetica: {pa}")


a1= int(input("Digite o 1° termo da PA: "))
n = int(input("Digite a quantidade de termos da PA: "))
r = int(input("Digite a razão da PA: "))

progressao_aritmetica(a1, n, r)
