text = 'Igor is learning python. Igor is improving his skills on python.'

# 1.count elements
counter = text.count('i'), text.count('o')
print(counter)

# 2.count elements
words = text.split(' ')
counter = 0

for word in words:
    if word == 'Igor':
        counter += 1

print(counter)
