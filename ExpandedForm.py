def expanded_form(num):
    result = []
    divider = 10
    while (divider < num):
        temp_var = num % divider
        if (temp_var != 0):
            result.insert(0,str(temp_var))
        num -= temp_var
        divider *= 10
    result.insert(0,str(num))
    return " + ".join(result)





print(expanded_form(12)) # Should return '10 + 2'
print(expanded_form(42)) # Should return '40 + 2'
print(expanded_form(70304)) # Should return '70000 + 300 + 4'