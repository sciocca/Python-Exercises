import math
def main():
    print("LADDER LENGTH")
    print()

    h = float(input("Height of ladder: "))
    ang = float(input("Angle (degrees): "))
    rad = (math.pi * ang)/180
    l = h/math.sin(rad)

    print("Length is: ", l)
main()