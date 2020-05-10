def solve(s):
    s.lower()
    sum = 0
    total_sums = []
    final_value = 0
    for i in s:
        if i == "a" or i == "e" or i == 'i' or i == 'o' or i == 'u':
            total_sums.append(sum)
            sum = 0
        else:
            index = ord(i) - 96
            sum += index
    for i in total_sums:
        if i > final_value:
            final_value = i
    return final_value

print(solve("zodiacs"))

