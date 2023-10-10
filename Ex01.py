'''Perguntar ao usuário quantos alunos tem
na sala e criar um array, unidimensional
(Vetor) com o nome de todos os alunos da
sala'''

alu = int(input("Quantos alunos tem na sala? "))
sala = [0]*alu
print("Qual o nome dos alunos?")
for x in range (alu):
    nome = input(f"Digite o {x+1}º nome: ")
    sala[x] = nome

for i in range (alu):
    print(sala[i], end =", ")