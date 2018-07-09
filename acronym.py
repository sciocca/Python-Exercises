phrase = input("What phrase do you wish to create into an acronym: ")
x = ""
for i in phrase.upper().split():
    x += i[0]
print(x)
