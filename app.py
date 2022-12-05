phrase = "This \"word\" is quoted. Amazing!"
separation = "______________________________"

print(phrase)
print(phrase.isupper())
print(len(phrase))
print(separation)

phrase = phrase.upper()

print(phrase.index("AM"))
print(phrase.isupper())
print(separation)

phrase = phrase.lower()

print(phrase[6])
print(phrase.isupper())
print(separation)

phrase = phrase.replace("amazing", "cool")

print(phrase)
print(phrase.islower())
print(separation)
