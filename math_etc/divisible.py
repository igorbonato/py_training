# numbers which are divisible by 7 but are not multiple to of 5 between 1 and 3201

for i in range(1, 3201):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
