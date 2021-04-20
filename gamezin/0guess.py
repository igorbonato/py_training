import random
n = random.randint(1, 50)
attempts = 1
totalGuesses = 10

print("LITTLE FUCKING GUESSING GAME\n")
print("********************************************\ngenerating random number between 0 to 50...")
print(
    f'number generated!\nyoull have {totalGuesses} chances...\n********************************************\n')

while attempts < totalGuesses:
    guess = int(input(f'Attempt number {attempts}: '))
    attempts = attempts + 1
    if guess == n:
        print("guessed!\nyou're great!\n")
        print(f'tries until guess: {attempts}')
        break
    elif guess > n:
        print("You missed! Shoot lower!\n\n")
    elif guess < n:
        print("You missed! Shoot higher!\n\n")
    else:
        print(f'You tried {attempts} times and lost! You suck!')
        break
