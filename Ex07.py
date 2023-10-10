'''Faça um código para ler 5 nomes de
usuários e suas respectivas senhas, e
armazenar cada lista em um array
diferente, após completar a digitação,
imprimir , nome, senha e posição dos
dados no array'''

nome_usuario = [0]*5
senha_usuario = [0]*5

for x in range (5):
    nome_usuario[x] = input("Digite seu nome: ")
    senha_usuario[x] = input("Digite sua senha: ")

print(f"\nOS dados das contas seguem: \n")
for y in range (5):
    print(f"O usuario da {y}º posição é {nome_usuario[y]}, tem a senha: {senha_usuario[y]}")