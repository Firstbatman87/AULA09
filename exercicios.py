# 1 ===================================================

num = int(input('Informe um número para saber sua tabuada(1 a 10): '))

for i in range(1, 11):
    print(f'{num} X {i:2} = {num * i}')

# 2 ==================================================

soma = 0

for i in range(1, 101):
    soma += i
print(soma)

# 3 ==================================================

for i in range(10, 0, -1):
    print(i)
print('FOGO!')

# 4 ==================================================

senha = ''

while senha != 'python123':
    senha = input('Digite a senha: ')
print('Acesso liberado!')