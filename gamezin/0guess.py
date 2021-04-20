import random
n = random.randint(1, 20)
attempts = 0
totalGuesses = 10

print("LITTLE FUCKING GUESSING GAME\n")
print("********************************************\ngenerating random number between 0 to 20...")
print(
    f'number generated!\nyoull have {totalGuesses} chances...\n********************************************\n')

while True:
    guess = int(input(f'Attempt number{attempts}'))
    if guess < n:
        print("You missed! Shoot higher!\n\n")
        # attempts = attempts + 1
    elif guess > n:
        print("You missed! Shoot lower!\n\n")
        # attempts = attempts + 1
    elif guess != n and attempts == 10:
        print(f'You tried {attempts} times and lost! You suck!')
        break
    else:
        print("guessed!\nyou're great!\n")
        print(f'tries until guess: {attempts}')
        break

for i in range(attempts, 0, +1):
    if
