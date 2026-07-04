import random

print("=" * 40)
print("🎮 Welcome to Number Guessing Game")
print("=" * 40)

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter a number between 1 and 100: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("Too low! 📉")
    elif guess > number:
        print("Too high! 📈")
    else:
        print(f"\n🎉 Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break

print("\nThanks for playing!")