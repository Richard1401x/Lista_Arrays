'''altere o exercício anterior para permitir
achar o nome de um aluno na lista'''

alu = int(input("Quantos alunos tem na sala? "))
sala = [0]*alu

for x in range (alu):
    nome = input(f"Digite seu nome: ")
    sala[x] = nome

consult = 0
perg = input("Você quer saber a posição de que aluno? ")
for i in range (alu):
    if perg == sala [i]:
        consult += 1
        print(f"{perg} esta na {i+1}º posição.")

if consult == 0:
    print("Nome não encontrado!")