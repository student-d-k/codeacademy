
people = {}

while True:
    name = input("Vardas: ").capitalize()
    if name:
        if not(name in people):
            people[name] = []
        for hobby in input("Pomegiai: ").lower().replace(',', ' ').split():
            if not(hobby in people[name]):
                people[name].append(hobby)
    else:
        if len(people) >=4:
            break

# people = {
#     'Jonas': ['krepsinis', 'zvejyba', 'medziokle', 'keliones'],
#     'Petras': ['krepsinis', 'zvejyba', 'keliones'],
#     'Kazys': ['zvejyba', 'medziokle'],
#     'Antanas': [],
#     'Gabrielius': ['keliones'],
#     'Zilvinas': ['krepsinis'],
#     'Juozas': [],
#     }

# people = {
#     'a': [1, 2, 3, 4],
#     'b': [2],
#     'c': [],
#     'd': [],
#     }

print(people)

max_hobby_pair = ''
max_hobby_count = 0
max_hobbies = []

for i, a in enumerate(people):
    for j, b in enumerate(people):
        if j <= i:
            continue
        hobbies = [value for value in people[a] if value in people[b]]
        n = len(hobbies)
        if n:
            print(f'{a} ir {b} turi {n} bendru(s) pomegiu(s) {hobbies}')
            if n > max_hobby_count:
                max_hobby_count = n
                max_hobby_pair = a + ' ir ' + b
                max_hobbies = hobbies

if max_hobby_count:
    print(f'Daugiausia bendru pomegiu ({max_hobby_count}) turi {max_hobby_pair}: {max_hobbies}')
