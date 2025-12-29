
def main(students, fan):
    count = 0

    for i, j in students:
        for f in j:
            if f == fan:
                count += 1
    return count


students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]
result = main(students, "Matematika")
print(result)