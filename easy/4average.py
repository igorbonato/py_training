while True:
    try:
        first_bi = float(input("ur first grade: "))
        if not 0 <= first_bi <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        sec_bi = float(input("ur second grade: "))
        if not 0 <= sec_bi <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        third_bi = float(input("ur third grade: "))
        if not 0 <= third_bi <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        four_bi = float(input("ur fourth grade: "))
        if not 0 <= four_bi <= 10:
            raise ValueError("0 - 10 ur dumbshit")
    except ValueError:
        print("OMG U ARE THE DUMBEST")

    else:
        break

result = first_bi + sec_bi + third_bi + four_bi
avg = result / 4
print('the poor average of ur grades is %.2f' % avg)
