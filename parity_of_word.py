#Compute the parity of a word
#Simple solution
def parity(s):
    s_b = ''.join(format(ord(x), 'b') for x in s)
    count = 0
    for digit in s_b:
        if digit == '1':
            count += 1
    if count % 2 != 0:
        return 1
    else:
        return 0



#print(parity('animal')) #0
#print(parity('sam')) #1

#what if we had to compute lots of large 64-bit words
#The above brute force solution is inefficient as it has to compute the binary of every string inputted, to make scalable i would suggest creating a lookup table with every character and it's count of # of 1s, therefore for any string inputted, we could loop through the string and assign a count of i's for each character
s = 'abcdefghijklmnopqrstuvwxyz'
lookup_dict = dict.fromkeys(s,0)
s_binary = ' '.join(format(ord(x), 'b') for x in s)
s_binary = s_binary.split(' ')
s_lookup = []
for item in s_binary:
    count = 0
    for digit in item:
        if digit == '1':
            count += 1
    s_lookup.append(count)
lookup_dict.update(zip(lookup_dict, s_lookup))
print(lookup_dict)

def complex_parity(s_list):
    final_list = []
    for word in s_list:
        counter_list = []
        for char in word:
            counter = lookup_dict[char]
            counter_list.append(counter)
        final = sum(counter_list)
        if final % 2 != 0:
            final_list.append(1)
        else:
            final_list.append(0)
    return final_list



#print(complex_parity(['abcde', 'sam', 'animal']))

#book methods using bitwise operators
def book_parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

#The first improvment is based on erasing the lowest set bit in a word in a single operation
#COMMIT TO MEMORY x&(x-1) equals x with its lowest set bit erased.
def book_parity_2(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

#using lookup tables
#this is not so important...gonna skip ahead