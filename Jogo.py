#Jogo adivinhe um número
import random 

#usuario escolhe um número
print('Irei escolher um número...')
User = int(input('Tente adivinhar o número:'))

Computer = random.randint(0,10)

while True:

    if User == Computer:
        print('Você acertou, eu escolhi o número {}'.format(Computer))
        print("Jogo encerrrado!!")
        break
        

    elif User!= Computer:
        print("Tente novamente")
        print('Você não acertou, eu escolhi o número {}'.format(Computer))
        User = int(input('Tente adivinhar o número:'))

    