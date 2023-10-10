'''Faça um código para ler 5 números e
armazenar em um vetor. Após a leitura
total dos 5 números, o código deve
escrever esses 5 números lidos na ordem
inversa'''

num = [0]*5

for x in range (5):
    perg = int(input(f"Digite o numero ({x+1}/5):  "))
    num[x] = perg

for y in range (4,-1,-1):
    print(num[y], end = " ")
    senha = input("Senha não identificada, tentar novamente: ")
else :
    print(nome_usuario[x],",login efetuado com sucesso!")