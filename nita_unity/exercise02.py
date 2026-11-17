
secret_number = 37
max_attempts = 6
attempts = 0
guess = 0

while guess != secret_number and attempts < max_attempts:
    guess = int(input("Your guess (1-100): "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")

if guess == secret_number:
    print(f"Correct! You found it in {attempts} attempts.")
else:
    print(f"Game over! The number was {secret_number}.")
