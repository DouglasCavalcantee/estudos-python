#pedir números ao usuário até que ele digite zero e mostrar a média dos números digitados
#mostrar quantos números foram digitados
# no final mostrar o resultado
soma = 0
contador = 0
while True:
    numero = float(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média dos números digitados é: {media}")
    print(f"Quantidade de números digitados: {contador}")
else:
    print("Nenhum número foi digitado.")