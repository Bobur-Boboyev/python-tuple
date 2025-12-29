emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))

ls = []

for i, j in emails:
    idx = j.index('@')
    domain = j[idx:]
    ls.append(domain)

print(ls)