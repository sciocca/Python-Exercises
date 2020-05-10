def tickets(people):
    change_on_hand = 0
    
    for i in people:
        if i == 25:
            change_on_hand += 25
        else:
            change_on_hand = change_on_hand - (i-25)
    
    if change_on_hand < 0:
            return "NO"
    return "YES"    

print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 25, 100]))