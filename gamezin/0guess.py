import random
n = random.randint(1, 100)
attempts = 1
totalGuesses = 10

print("LITTLE FUCKING GUESSING GAME\n")
print("********************************************\ngenerating random number between 0 to 100...")
print(
    f'number generated!\nyoull have {totalGuesses} chances...\n********************************************\n')

while attempts < totalGuesses:
    guess = int(input(f'Attempt number {attempts}: '))
    attempts = attempts + 1
    if guess == n:
        print("\nGUESSED!!!\nyou're great!\n")
        print(f'tries until guess: {attempts}')
        break
    elif guess > n:
        print("You missed! Shoot lower!\n")
    elif guess < n:
        print("You missed! Shoot higher!\n")
    else:
        print(f'You tried {attempts} times and lost! You suck!')
        break
