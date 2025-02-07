import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    return random_number

if __name__ == "__main__":
    mmax_attempts = 7
    random_number=number_guessing_game()
    #print("random_number:", random_number)

    for max_attempts in range(mmax_attempts-1, -1,-1):
        n=int(input("deviner un nombre entier entre [1, 100] ? ") )
        max_attempts -= 1

        if max_attempts==-1:
            print("perdu, aucune tentative est bonne ! il fallait le nombre=",random_number)
            break
        elif n > random_number:
            print("Too high! c'est pas bon, essayez encore, nb de tentative restante=", max_attempts+1,"\n")
        elif n < random_number:
            print("Too low! c'est pas bon, essayez encore, nb de tentative restante=", max_attempts+1,"\n")
        else:
            print("bravo, c'est bon, le nombre était bien =>", random_number)
            break
