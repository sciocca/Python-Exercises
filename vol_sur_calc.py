import math


def main():
    print("Volume and Surface Area of a Sphere")
    print()

    r = float(input("What is the radius: "))

    vol = 4/3 * math.pi * r ** 3
    sur = 4 * math.pi * (r ** 2)

    print()
    print("The Volume is: ", vol)
    print("The Surface Area is: ", sur)
main()

