#ints, char, etc. Tho in python everything is an object like JavaScript
#Bitwise operations: 
#&	Bitwise AND	            x & y
#|	Bitwise OR	            x | y
#~	Bitwise NOT	            ~x
#^	Bitwise XOR	            x ^ y
#>>	Bitwise right shift	    x>>
#<<	Bitwise left shift	    x<< 
#counting_bits in a nonnegative interger

def count_bits(n):
    num_bits = 0
    while n:
        num_bits += n & 1 #sets bit
        n >>= 1
    return num_bits

print(count_bits(12))

#1. Know the bitwise operators
#2. Understand masks and create them in machine independent ways
#3. Signedness and its implications in shifting
#4. Consider the cache
#5. Commutativity and associativity, can use to preform parallel operations or reorder them

#negative numbers are their 2's complement value
#key methods
#abs(-34.5), math.ceil(2.17), math.floor(3.14), min(x,-4), max(3.14,y), pow(2.17, 3.14), math.sqrt(225)
# interconversion of strings and intergers eg.
# str(42), int('42'), float('42.14)
# Float infinity = float('inf')
# When comparing floating points consider math.isclose()
# key random methods
# random.randrange(28) Return a randomly selected element from range(start, stop, step). 
# random.randint(8,16),
#  random.random(), Return the next random floating point number in the range [0.0, 1.0). 
# random.shuffle(A) Shuffle a list
# random.choice(A) Chose a random element from a list