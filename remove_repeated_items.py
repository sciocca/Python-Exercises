def remove_repeats(a):
    result = []
    for x in a:
        if x not in result:
            result.append(x)
    return result




print(remove_repeats([1,1,3,3,3,5,7,11,11,13]))