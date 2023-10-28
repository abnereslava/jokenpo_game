import random
pedra = "pedra"
papel = "papel"
tesoura = "tesoura"
opcoes = [pedra, papel, tesoura]

while True:
    escolha_user = input("Pedra, papel ou tesoura? Digite sua escolha: \n")
    escolha_user = escolha_user.lower()

    if escolha_user != "pedra" and escolha_user != "papel" and escolha_user != "tesoura":
        print("Escolha uma opção válida!")
    else:
        break    

escolha_comput = random.choice(opcoes)
print(f"Você escolheu {escolha_user} e eu escolhi {escolha_comput}.")

condvitoria = escolha_user == pedra and escolha_comput == tesoura or escolha_user == papel and escolha_comput == pedra or escolha_user == tesoura and escolha_comput == papel
condempate = escolha_user == escolha_comput

if not condvitoria and not condempate:
    print("Que pena! Você perdeu.")

if condvitoria:
    print("Parabéns! Você ganhou!")

if condempate:
    print("Parece que deu empate...")