
people = {
    'Petras': ['krepsinis', 'zvejyba', 'keliones'],
    'Kazys': ['zvejyba', 'medziokle'],
    'Antanas': [],
    'Gabrielius': ['keliones'],
    'Zilvinas': ['krepsinis'],
    'Juozas': [],
    'Jonas': ['krepsinis', 'zvejyba', 'medziokle', 'keliones'],
    }

# print(people)
# print()

# sukuriam tuscia zodyna su visomis imanomomis zmoniu poromis

pairs = {}

for a in people:
    for b in people:
        if a == b:
            break
        pairs[(a, b)] = []

# priskiriam zodynui lista su bendru pomegiu kiekiu ir bendru pomegiu sarasu

for p in pairs:
    l = [v for v in people[p[0]] if v in people[p[1]]]
    if l:
        pairs[p] = [len(l), l]
    else:
        pairs[p] = [len(l)]

# max bendru pomegiu

max_val = max(pairs.values())[0]

for key, val in pairs.items():
    if val[0] == max_val:
        print(f'daugiausia bendru pomegiu: {key}, {val[1]}')

print()

# x bendru pomegiu

x = 1

for key, val in pairs.items():
    if val[0] == x:
        print(f'{x} bendru pomegiu: {key}, {val[1]}')
