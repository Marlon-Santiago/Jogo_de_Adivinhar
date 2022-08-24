import random


print('*________________________________*')
print('Bem vindo ao jogo de adivinhação')
print('*________________________________*')
print()

numero_secreto = random.randrange(1, 100)
total_de_tentativas = 0
pontos = 1000

print('Qual o nível de dificuldade você deseja ?')
print('(1) fácil (2) Medio (3) difícil')

nivel = int(input('Defina o nível desejado: '))
print()


if nivel == 1:
    print('Você escolheu o nível Facil')
    total_de_tentativas = 20

elif nivel == 2:
    print('Você escolheu o nível Medio')
    total_de_tentativas = 10

else:
    print('Você escolheu o nível Difícil')
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    chute = input('Digite um número de 1 a 100 ')
    print(f'Você esta na rodada {rodada} de {total_de_tentativas} rodadas ')
    print()
    chute = int(chute)
    print(f'Você digitou {chute} ')
    print()

    if chute < 1 or chute > 100:
        print('Você deve digitar um numero entre 1 e 100')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f'Você acertou , o número secreto é {numero_secreto} e fez {pontos} pontos')
        print()
        break

    elif maior:
        print('Você digitou um número maior que o número secreto')

    else:
        print('Você digitou um número menor que o número secreto')
    pontos_perdidos = abs(numero_secreto - chute)
    pontos  -= pontos_perdidos

if chute == numero_secreto:
    print()
    print('VOCÊ GANHOU')

else:
    print()
    print(f'GAME OVER ! o núero secretro era {numero_secreto} e vocÊ ficou com {pontos} pontos')

