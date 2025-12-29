numbers = (3, 6, 7, 8, 10, 11)

ls = []

for i in numbers:
    if i % 2 == 0:
        ls.append(i)

result = tuple(ls)

print(result)