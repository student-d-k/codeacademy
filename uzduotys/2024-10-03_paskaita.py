
#1

# import calendar

# all_y = range(1900, 2050)
# ly = list(filter(calendar.isleap, all_y))

# print(ly)

# 2

# l = [1, 2, 3, 4, 5]
# naujas = [x ** 2 for x in l]

# print(naujas)

#3

class Zmogus:

    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return " ".join([self.vardas, str(self.amzius)])

l = [Zmogus('Jonas', 30), Zmogus('Jonas', 15), Zmogus('Petras', 32), Zmogus('Jolanta', 28)]

print(sorted(l, key = lambda x: (x.vardas, x.amzius)))

from operator import attrgetter

print(sorted(l, key = attrgetter('amzius')))

print(sorted(l, key = lambda x: (x.vardas), reverse=True))
