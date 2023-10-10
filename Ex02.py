'''altere o exercício anterior e mostre na tela,
ao final, o nome de cada aluno e sua
respectiva posição no array.'''

alu = int(input("Quantos alunos tem na sala? "))
sala = [0]*alu

for x in range (alu):
    nome = input(f"Digite o {x+1}º nome: ")
    sala[x] = nome

for i in range (alu):
    print(f"O aluno {sala[i]}, esta na {i+1}º posição")