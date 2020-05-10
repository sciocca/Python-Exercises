def multiply(x,y):
    sign = -1 if (x[0] < 0) ^ (y[0] < 0) else 1
    x[0], y[0] = abs(x[0]), abs(y[0])
    result = [0] * (len(X) + len(y))
    for i in reversed(range(len(x))):
        for j in reversed(range(len(y))):
            result[i + j + 1] += x[i] * y[j]
            result[i +j] += result[i + j + 1]
            result[i + j + 1] %= 0
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]
    

            




print(multiply([1,2,3],[-4,5,6]))


#multiply two arrays like baby math