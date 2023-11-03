from time import sleep
import random
possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']

print('\nAproxime-se desafiante...')
sleep(0.5)
print('SEJA BEM VINDO AO DESAFIO JÓ KEN PÔ!')
sleep(1)
vitorias = 0
derrotas = 0

def pedrapapeltesoura():
    print("\nVocê já sabe as regras...")
    sleep(0.5)
    escolha_user = str(input('Portanto, qual você escolhe: pedra, papel ou tesoura? ').strip()).upper()
    if escolha_user in possibilidades:
        escolha_cpu = random.choice(possibilidades)
        print("Então vamos lá!\n")
        sleep(0.5)
        print('JÓ')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PÔ!\n')
        sleep(0.5)
        if escolha_user == 'PEDRA' and escolha_cpu == 'TESOURA' or escolha_user == 'PAPEL' and escolha_cpu == 'PEDRA' or escolha_user == 'TESOURA' and escolha_cpu == 'PAPEL':
            if escolha_user == "PEDRA": escolha_user = escolha_user.replace("PEDRA", "pedra 👊")
            if escolha_user == "PAPEL": escolha_user = escolha_user.replace("PAPEL", "papel 🖐️")
            if escolha_user == "TESOURA": escolha_user = escolha_user.replace("TESOURA", "tesoura ✌️")
            if escolha_cpu == "PEDRA": escolha_cpu = escolha_cpu.replace("PEDRA", "pedra 👊")
            if escolha_cpu == "PAPEL": escolha_cpu = escolha_cpu.replace("PAPEL", "papel 🖐️")
            if escolha_cpu == "TESOURA": escolha_cpu = escolha_cpu.replace("TESOURA", "tesoura ✌️")
            print(f'Parece que você escolheu: {escolha_user}.')
            sleep(1)
            print(f'Eu escolhi: {escolha_cpu}.')
            sleep(1)
            print('\n...')
            sleep(1)
            print('Você venceu...')
            sleep(1)
            global vitorias
            vitorias += 1
            revanche()
        elif escolha_user == 'TESOURA' and escolha_cpu == 'PEDRA' or escolha_user == 'PEDRA' and escolha_cpu == 'PAPEL' or escolha_user == 'PAPEL' and escolha_cpu == 'TESOURA':
            if escolha_user == "PEDRA": escolha_user = escolha_user.replace("PEDRA", "pedra 👊")
            if escolha_user == "PAPEL": escolha_user = escolha_user.replace("PAPEL", "papel 🖐️")
            if escolha_user == "TESOURA": escolha_user = escolha_user.replace("TESOURA", "tesoura ✌️")
            if escolha_cpu == "PEDRA": escolha_cpu = escolha_cpu.replace("PEDRA", "pedra 👊")
            if escolha_cpu == "PAPEL": escolha_cpu = escolha_cpu.replace("PAPEL", "papel 🖐️")
            if escolha_cpu == "TESOURA": escolha_cpu = escolha_cpu.replace("TESOURA", "tesoura ✌️")
            print(f'Parece que você escolheu: {escolha_user}.')
            sleep(1)
            print(f'Eu escolhi: {escolha_cpu}.')
            sleep(1)
            print('\n...')
            sleep(1)
            print('HA, HÁ... Eu ganhei! ̶ ̶o̶t̶á̶r̶i̶o̶ ')
            sleep(1)
            global derrotas
            derrotas += 1
            revanche()
        elif escolha_cpu == escolha_user:
            if escolha_user == "PEDRA": escolha_user = escolha_user.replace("PEDRA", "pedra 👊")
            if escolha_user == "PAPEL": escolha_user = escolha_user.replace("PAPEL", "papel 🖐️")
            if escolha_user == "TESOURA": escolha_user = escolha_user.replace("TESOURA", "tesoura ✌️")
            if escolha_cpu == "PEDRA": escolha_cpu = escolha_cpu.replace("PEDRA", "pedra 👊")
            if escolha_cpu == "PAPEL": escolha_cpu = escolha_cpu.replace("PAPEL", "papel 🖐️")
            if escolha_cpu == "TESOURA": escolha_cpu = escolha_cpu.replace("TESOURA", "tesoura ✌️")
            print(f'Parece que você escolheu: {escolha_user}.')
            sleep(1)
            print(f'Eu escolhi: {escolha_cpu}.')
            sleep(1)
            print('\n...')
            sleep(1)
            print('Deu empate. Vamos tentar de novo!')
            sleep(1)
            pedrapapeltesoura()
        else:
            print("Essa é uma opção inválida. Tente novamente.")
            pedrapapeltesoura()
    else:
        print("Essa é uma opção inválida. Tente novamente.")
        pedrapapeltesoura()

def revanche():
    revanche = input('Quer jogar de novo? [sim/não]: ').lower()
    revanche = revanche.strip()
    if revanche == 'sim':
        print('\nEntão bora!')
        pedrapapeltesoura()
    elif revanche == 'não' or revanche == 'nao':
        print('\nOh, que pena...\n')
        sleep(1)
        resultados()
    else:
        print("Essa é uma opção inválida. Tente novamente.")
        pedrapapeltesoura()

def resultados():
    print("Bem... isso foi divertido, mas vamos ao que interessa...")
    sleep(1.5)
    print("Seus resultados são...\n")
    sleep(1)
    print(f'Vitórias: {vitorias}.')
    sleep(1)
    print(f'Derrotas: {derrotas}\n')
    sleep(1)
    if vitorias == derrotas:
        print('Parece que dessa vez empatamos.')
        sleep(0.5)
        print('Mas garanto que te venço na próxima.')
        sleep(1)
        print('Até mais!')
    elif vitorias > derrotas:
        print("...")
        sleep(1.5)
        print("Ainda não sei como...", end=' ')
        sleep(1)
        print('mas tenho certeza que você trapaceou.')
        sleep(1)
        print("Hmpf... parabéns, você ganhou.")
        sleep(0.5)
        print('Agora suma da minha frente.')
    else:
        print("Como era de se esperar: eu venci!")
        sleep(1)
        print('Admita...', end=' ')
        sleep(1)
        print('você nunca teve chance contra minha incrível habilidade!')
        sleep(1)
        print('Sempre que quiser levar uma surra no JÓ KEN PÔ, estarei aqui.')
        print('Adeus.')

pedrapapeltesoura()
