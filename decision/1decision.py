def Average(self):
    avg = sum(self) / len(self)
    return avg


name0 = input("first name student: ")
name1 = input("second name student: ")
name2 = input("third name student: ")


while True:
    print("\nSTUDENT", name0.upper())
    try:
        stud0_0 = float(input("0-10\nfirst grade: "))
        if not 0 <= stud0_0 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        stud0_1 = float(input("second grade: "))
        if not 0 <= stud0_1 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        stud0_2 = float(input("third grade: "))
        if not 0 <= stud0_2 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
    except ValueError:
        print("OMG U ARE THE DUMBEST")
    break

while True:
    print("\nSTUDENT", name1.upper())
    try:
        stud1_0 = float(input("0-10\nfirst grade: "))
        if not 0 <= stud1_0 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        stud1_1 = float(input("second grade: "))
        if not 0 <= stud1_1 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        stud1_2 = float(input("third grade: "))
        if not 0 <= stud1_2 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
    except ValueError:
        print("OMG U ARE THE DUMBEST")
    break

while True:
    print("\nSTUDENT", name2.upper())
    try:
        stud2_0 = float(input("0-10\nfirst grade: "))
        if not 0 <= stud2_0 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        stud2_1 = float(input("second grade: "))
        if not 0 <= stud2_1 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
        stud2_2 = float(input("third grade: "))
        if not 0 <= stud2_2 <= 10:
            raise ValueError("0 - 10 ur dumbshit")
    except ValueError:
        print("OMG U ARE THE DUMBEST")
    break

# mean of the students
# stud1
sum_grades0 = [stud0_0, stud0_1, stud0_2]
average0 = Average(sum_grades0)

# stud2
sum_grades1 = [stud1_0, stud1_1, stud1_2]
average1 = Average(sum_grades1)

# stud3
sum_grades2 = [stud2_0, stud2_1, stud2_2]
average2 = Average(sum_grades2)

print(f'\n{name0} %.1f' % average0, f'\n{name1} %.1f' %
      average1, f'\n{name2} %.1f' % average2)
if average0 > average1 and average0 > average2:
    print(f'\n\n{name0} has the better grades')
elif average1 > average1 and average1 > average2:
    print(f'\n\n{name1} has the better grades')
elif average2 > average0 and average2 > average1:
    print(f'\n\n{name2} has the better grades')
elif average0 == average1:
    print(f'\n{name0} has the same average grades as {name1}')
elif average1 == average2:
    print(f'\n{name2} has the same average grades as {name1}')
elif average0 == average2:
    print(f'\n{name0} has the same average grades as {name2}')
else:
    print('wtf')


# all_average = average0, average1, average2
# list_average = sorted(all_average, reverse=True)
# print(list_average)

# print(f'\n\n{name0} %.1f' % average0, f'\n{name1} %.1f' %
#       average1, f'\n{name2} %.1f' % average2)
