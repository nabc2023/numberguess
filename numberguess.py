import random

def guess_number():
    random_number = random.randint(1, 10)
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        if user_guess == random_number:
            print("You guessed it! The number was", random_number)
            break
        elif user_guess < random_number:
            print("Too low! Guess again.")
        elif user_guess > random_number:
            print("Too high! Guess again.")

if __name__ == '__main__':
    guess_number()