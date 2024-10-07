# def intersection(lst1, lst2):
#     return list(set(lst1) & set(lst2))

# # Driver Code
# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# print(intersection(lst1, lst2))

# def intersection(lst1, lst2):
#     lst3 = [value for value in lst1 if value in lst2]
#     return lst3

# Driver Code
lst1 = [4, 9, 1, 9, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
# print(intersection(lst1, lst2))

print(set(lst1) & set(lst2))

i = []

for e in lst1:
    if e in lst2 and not(e in i):
        i.append(e)

print(i)

print([value for value in lst1 if (value in lst2) and (value > 20)])