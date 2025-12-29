words = ("apple", "banana", "strawberry", "kiwi")

mx = words[0]

for i in words:
    if len(i) > len(mx):
        mx = i

print(mx)
