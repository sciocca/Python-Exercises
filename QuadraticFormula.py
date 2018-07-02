import math

def main():
    print("Quadratic Formula Program")
    print()

    a = float(input("Coefficient a: "))
    b = float(input("Coefficient b: "))
    c = float(input("Coefficient c: "))

    discroot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discroot) / (2 * a)
    root2 = (-b - discroot) / (2 * a)

    print()
    print("The roots are: ", root1, root2)


main()