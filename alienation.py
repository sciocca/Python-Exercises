def alienate(a):
    a.sort()
    print(a)
    b = []
    i = 1
    for index1,item1 in enumerate(a):
        if (index1 == 0 or index1 % 2 == 0):
            b.append(item1)
        else:
            b.append(a[len(a) - i]) 
            i += 1
    return b

#book
def rearrange(A):
    for i in range(len(A)):
        A[i: i + 2] = sorted(A[i : i + 2], reverse=i%2)



print(alienate([1,8,5,2,20,14,30,82,21,6]))
#alienate means a[0] <= a[1] >= b[1] <= b[2]