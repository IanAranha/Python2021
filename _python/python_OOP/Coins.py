def coins(nbr):
    change=[]
    total_left = nbr
    Twentyfive_cents = 0
    Ten_cents = 0
    Five_cents = 0
    One_cents = 0

    while total_left > 24:
        Twentyfive_cents += 1
        total_left -= 25
    while total_left > 9:
        Ten_cents += 1
        total_left -= 10
    while total_left > 4:
        Five_cents += 1
        total_left -= 5
    while total_left > 0:
        One_cents += 1
        total_left -= 1
    change.append(Twentyfive_cents)
    change.append(Ten_cents)
    change.append(Five_cents)
    change.append(One_cents)
    return change

print(coins(29))
print(coins(80))
print(coins(24))
print(coins(89))
print(coins(93))