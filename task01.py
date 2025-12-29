def get_max_age(people):
    name, max_age = people[0]

    for i, j in people:
        if j > max_age:
            name = i
            max_age = j

    return f"{name} - {max_age} yosh"

people = [("Ali", 34), ("Laylo", 30), ("Jasur", 19)]
result = get_max_age(people)

print(result) 