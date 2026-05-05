numero = int(input("Digite um número para calcular o fatorial: "))

if numero >= 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item
        print(f"Passo: {item} -> {fatorial}")
        
    print(f"O fatorial de {numero} é: {fatorial}")
else:
    print("Por favor, digite um número inteiro não negativo.") 
