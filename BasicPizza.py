import math


def main():
    print("Cost per square inch of pizza given diameter and price")
    print()

    dia = float(input("Diameter of the Pizza: "))
    price = float(input("Price of the Pizza: "))

    r = dia/2
    area = math.pi * r ** 2
    ans = price/area

    print()
    print("The Price per square inch is: ", ans)

main()