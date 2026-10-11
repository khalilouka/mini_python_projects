import random

def play_guessing_game():
    number_of_guesses= 0
    # verfier le choix de la difficulté
    while True:
        difficulty = input("Choisie la difficulté (facile, moyen, difficile)(f/m/d) : ").strip().lower()
        if not difficulty in ("f", "m", "d"):
            print("Ton entrée ne fais pas partie des choix donnés.")
            continue 
        else:
            break
    # demander a user selon la difficulté et creer le nombre recherché 
    if difficulty == "f":
        number_to_guess = random.randint(1, 10)
        print("devinez le nombre entre 1 et 10(1 et 10 inclus)")
    elif difficulty == "m":
        number_to_guess = random.randint(1, 50)
        print("devinez le nombre entre 1 et 50(1 et 50 inclus)")
    elif difficulty == "d":
        number_to_guess = random.randint(1, 100)
        print("devinez le nombre entre 1 et 100(1 et 100 inclus)")

    while number_of_guesses < 5:
        user_number = input("Ton choix: ")
        if not user_number.isdigit():       # verifiez si l'entré est un nombre
            print("Entrée invalide. Tapez un chiffre.")
            continue

        user_number = int(user_number)      # transformer le input de str en int

        if difficulty == "f":
            if not (1 <= user_number <= 10):    #verifiez si l'entré est entre 1 et 10
                print("Attention, le nombre doit être entre 1 et 10.")
                continue
        elif difficulty == "m":
            if not (1 <= user_number <= 50):    #verifiez si l'entré est entre 1 et 10
                print("Attention, le nombre doit être entre 1 et 50.")
                continue
        elif difficulty == "d":
            if not (1 <= user_number <= 100):    #verifiez si l'entré est entre 1 et 10
                print("Attention, le nombre doit être entre 1 et 100.")
                continue

        number_of_guesses+=1     # incrementer le nombre d'essais

        if user_number == number_to_guess:
            print(f"Bingo! number of guess : {number_of_guesses}")
            break
        elif user_number > number_to_guess:
            print("Wrong answer! Try lower")
        else:
            print("Wrong answer! Try higher")

    else:       # ce code s'execute que si y'as pas de break et nombre-de guesses = 5
        print(f"Nombre d'essais términé ! You lose !!! Le nombre a trouvé été {number_to_guess}")

def main():
    while True:
        play_guessing_game()
        #Demander au joueur si il refait une partie
        replay = input("Tu veux rejouer ? (o/n)").strip().lower()       
        if not replay in ("o", "oui", "y", "yes"):
            print("Merci d'avoir joué!")
            break

if __name__ == "__main__":
    main()