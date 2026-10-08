# 1 - Crie uma lista com 5 filmes favoritos, mostre o primeiro, o último e o total

filmes = ['Homem-Aranha', 'Matrix', 'Arqueiro Verde', 'Carros', 'Hulk']
print(f'Primeiro: {filmes[0]},\nÚltimo: {filmes[-1]},\nTotal: {len(filmes)}')

# 2 - Peça 5 números, guarde em uma lista e mostre o maior, o menor e a soma (max, min, sum)

numeros = []

for i in range(1, 6):
    numeros.append(int(input(f'Número {i}: ')))

print(f'Maior: {max(numeros)}\nMenor: {min(numeros)}\nSoma: {sum(numeros)}.')

# 3 - Crie um dicionário com os dados de um celular (marca, modelo, preço) e mostre cada par chave-valor com 
# for chave, valor in dicionario.items()

celular = {
    'Marca': 'P',
    'Modelo': 'O',
    'Preço': 2000
}