'''Escreva um código que permita a leitura
das notas de uma turma de 5 alunos e
guarde num vetor, Calcular a média da
turma e contar quantos alunos obtiveram
nota acima desta média calculada
Escrever a média da turma e o resultado
da contagem'''

alunos = [0]*5
nota_fin = 0
acim = 0
print("Leremos a nota dos 5 alunos da turma. \n")
for x in range (5):
    nota_ind = float(input(f"Nota do {x+1}º aluno: "))
    alunos [x] = nota_ind

for y in range (5):
    nota_fin += alunos[y]
media = nota_fin / 5

for z in range (5):
    if alunos[z] >= media:
        acim += 1

print(f"A média da turma foi {media}.\n"
      f"Vemos que {acim} alunos tiraram uma nota acima dessa média.")