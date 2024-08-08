A = int(input("Digite o 1º número inteiro: "))
B = int(input("Digite o 2° número inteiro: "))

if A < B:
    soma = 0
    for i in range(A, B + 1):
        soma += i
    print(f"A soma dos números inteiros no intervalo [{A}, {B}] é: {soma}")

    # O primeiro número não deve ser menor que o segundo se não vai dar PT (eror)

else:
    print("Erro: o 1º número e menor que o 2°.")
