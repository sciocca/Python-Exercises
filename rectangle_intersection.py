import collections
Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))
#x,y is leftmost point
#width and height are self explanatory
#eg Rectangle(2,1,3,4) is a rectangle with the points (2,1), (5,1), (2,5), (5,5)
#defining it with variables is (x,y), (x + width, y), (x, y + height), (x + width, y + height)
#So we want to take 2 rectangles and check if they intersect,  ?It is easier to tell if rectangles dont intersect. so I will start with that, we can create a list of logical conditions which must be met for each rectangle
#R1.x, R1.y, R1.width, R1.height, R2.x, R2.y, R2.width, R2.height
#R1.X <= R2.X + R2.width
#R1.x + R1.width >= R2.x
#R1.Y <= R2.Y + R2.height
#R1.Y + R1.height >= R12.Y
def intersection(R1,R2):
    def is_intersection(R1,R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)
    if not is_intersection(R1,R2):
        return (0,0,-1,-1)
    return Rectangle (max(R1.x, R2.x), max(R1.y, R2.y),min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x), min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))


print(intersection((1,1,3,4),(2,3,3,3)))

#How to understand the problem
#How to define if two rectangles are intersecting. If the leftmost point is smaller than the length of the side being measured and vis versa
#The intersection rectangle is defined as Rectangle (max x, max y, min width - max x, min height - max y)