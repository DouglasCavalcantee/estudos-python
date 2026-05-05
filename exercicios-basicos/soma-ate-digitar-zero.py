#pedir números ao usuário até que ele digite zero e somar todos os números digitados
# no final mostrar o resultado

soma = 0
contador = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
    contador += 1

print(f"A soma total dos números digitados é: {soma}")
print(f"Quantidade de números digitados: {contador}")