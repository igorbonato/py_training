# first method

number = int(input('tell me ur number!: '))

factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print(factorial)

# second method

number = int(input('tell me ur number!: '))


def fact(value):
    if value == 1:
        return 1
    else:
        return value * fact(value - 1)


print(fact(number))
