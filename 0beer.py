while True:
    beernum = int(input("how many bottles of beer? "))
    if beernum <= 1:
        print("more than 1 beer ur fucking asshole")
    elif beernum > 10000:
        print("u fucking drunk, just 10000 bottles. no more than that")
    else:
        break

for i in range(beernum, 0, -1):
    if i == 1:
        print(i, "bottle of beer".upper())
        print("        i drink and i finish it!")
    else:
        print(i, "bottles of beer".upper())
        print("       i drink one, throw it in the trash")
