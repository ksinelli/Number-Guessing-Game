import random

NUMBER = random.randint(1, 100)

def start_game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    is_choosing_difficulty = True

    while is_choosing_difficulty:

        difficulty = input("Choose a difficulty.  Type 'easy' or 'hard':").lower()

        if difficulty == "easy":
            number_of_guesses = 10
            is_choosing_difficulty = False
            # return number_of_guesses
        elif difficulty == "hard":
            number_of_guesses = 5
            is_choosing_difficulty = False
            # return number_of_guesses
        else:
            print("Sorry, I didn't understand that.")

    begin_guessing(number_of_guesses)

def begin_guessing(num_of_guesses):
    i = num_of_guesses
    while num_of_guesses > 0:
        print(f"You have {num_of_guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < 1 or guess > 100:
            print("Please choose a number between 1 and 100.")
        elif guess == NUMBER:
            print("That's it!  You win!  Good job!")
            exit()
        elif guess > NUMBER:
            print("Too high.")
            num_of_guesses -= 1
            if not num_of_guesses == 0:
                print("Guess again.")
        elif guess < NUMBER:
            print("Too low.")
            num_of_guesses -= 1
            if not num_of_guesses == 0:
                print("Guess again.")
    print(f"You ran out of guesses!  The correct number was {NUMBER}.")
    print("Better luck next time!")

start_game()
