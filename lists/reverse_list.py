list1 = [10, 20, 30, 40, 50]
list2 = []

for index in range(-1, -len(list1)-1, -1):
    list2.append(list1[index])
print(list2)
