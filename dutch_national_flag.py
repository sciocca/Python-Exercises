def dutch_nat_flag_1(pivot_index,list):
    index = list[pivot_index]
    less_than, equal_to, greater_than = [], [], []
    for i in list:
        if i < index:
            less_than.append(i)
        if i == index:
            equal_to.append(i)
        if i > index:
            greater_than.append(i)
    return less_than + equal_to + greater_than

def dutch_nat_flag_2(pivot_index, list):
    index = list[pivot_index]
    small = 0
    for i in range(len(list)):
        if list[i] < index:
            list[i], list[small] = list[small], list[i]
            small += 1
    large = len(list) - 1
    for i in reversed(range(len(list))):
        if list[i] > index:
            list[i], list[large] = list[large], list[i]
            large -= 1    
    return list





print(dutch_nat_flag_2(3,[0,1,2,0,2,1,1]))
print(dutch_nat_flag_2(1,[0,1,2,0,2,1,1]))