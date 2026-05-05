def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

meses = 8
valor_base = 100

for i in range(1, meses + 1):
    investimento = fibonacci(i) * valor_base
    print(f'Mês {i}: R$ {investimento}')