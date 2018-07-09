def main():
    name = input("Input Name: ")
    namelist = name.split()

    value = 0
    for word in namelist:
        for ch in word:
            value = value + ord(ch.lower()) - ord("a") + 1

    print("Numerological Value: ", value)


main()


