# Sua solução aqui

# Enunciado: 
# Faça um programa para entrar com 5 números 
# e imprimir a média desses números.

# Variavel para armazenar o somatorio
soma = 0

# Leitura de dados e armazenamento deles
# na variavel de somatorio
for i in range(5):
    numero = float(input())
    soma += numero

# Calculo da media
media = soma / 5

# Saida de dados
print(f"{media:.2f}")