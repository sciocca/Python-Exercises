import math
def main():
    print("Slope and Distance Formula")
    print()

    x1 = int(input("Input first point x: "))
    x2 = int(input("Input second point x: "))
    y1 = int(input("Input first point y: "))
    y2 = int(input("Input second point y: "))

    slope = (y2 - y1)/(x2 - x1)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("The Slope is: ", slope, "The Distance is: ",distance)
main()
