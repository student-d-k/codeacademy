
l = [1, 2, 3, 4]

# variantas 1

# new_l = []

# for i, e in enumerate(l):
#     print(i)
#     if i < len(l)-1:
#         new_l.append(e ** l[i+1])
#     else:
#         new_l.append(e)

# variantas 2

new_l = [e ** l[i + 1] if i < len(l)-1 else e for i, e in enumerate(l)]

# rezultatas

print(l)
print(new_l)

# ?

items = {'1001': 15, '1002': 9, '1003': 17.5}

def sum_price(items: dict) -> float:
    x = sum(items.values())
    if x > 100:
        return x * 0.9
    else:
        return x

print(sum_price(items))
