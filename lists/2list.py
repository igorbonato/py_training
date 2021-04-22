# testing first and last element

test_list = [12, 54, 86, 7, 90, 10]

if test_list[0] == test_list[-1]:
    print('true')
else:
    print('false')


# divisible for 5 or not

num_list = [50, 10, 24, 60, 12, 78, 104, 100]

for num in num_list:
    if num % 5 == 0:
        print('here number divisibles for 5: ', num)
    else:
        pass
