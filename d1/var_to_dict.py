d = [("Hendrix", "1942"), ("Allman", "1946"), ("King", "1925"), ("Clapton", "1945")]
dictionar = dict()

for el in d:
    dictionar.update({el[1]: el[0]})
    # dictionar[el[1]] = el[0]
print(sorted(dictionar.items(), reverse=True))
