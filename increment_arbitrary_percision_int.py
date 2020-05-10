def increment_1(D):
    D = ''.join([str(e) for e in D])
    D = int(D) + 1
    D = [int(x) for x in str(D)]
    return D

#print(increment_1([1,2,9]))
#in python lists can be arbitrarily long so we can easily use list methods to create the digit add 1, and return the list

#do by grade school math aka
# 1 2 9
#+    1
#-------
#1 3 0

def increment_2(D):
    D[-1] += 1
    for i in reversed(range(1,len(D))):
        if D[i] != 10:
            break
        D[i] = 0
        D[i - 1] += 1
    if D[0] == 10:
        D[0] = 1
        D.append(0)
    return D

print(increment_2([1,2,9]))