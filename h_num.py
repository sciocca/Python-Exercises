#The input is a list of citations for his papers
def h_index_calc(c_count):
    c_count.sort()
    n = len(c_count)
    for i,c in enumerate(c_count):
        if c >= n - i:
            return n - i
    return 0



print(h_index_calc([1,4,1,4,2,1,3,5,6]))