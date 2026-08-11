import random

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

secret_number = random.randint(start, end)

while True:
    guess = int(input(f"Guess the number between {start} and {end}: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break