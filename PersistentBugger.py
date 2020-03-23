
def persistence(n):
    pres = list(map(int, str(n)))
    if (n < 10):
        return 0
    else:
        product = 1
        for i in pres:
            product = product * i
        return 1 + persistence(product)



print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
print(persistence(999), 4)

