
import datetime


class JournalRecord:

    def __init__(self, name: str, amount: float) -> None:
        self.__time_created = datetime.datetime.now().strftime('%Y %m %d')
        self.name = name
        self.amount = amount

    def __str__(self) -> str:
        return f'{self.__time_created}> {self.name}: {self.amount:.2f}'


class Budget:

    def __init__(self) -> None:
        self.__journal = []

    def add_record(self, jr: JournalRecord) -> None:
        self.__journal.append(jr)

    def pop_record(self, i: int) -> JournalRecord:
        return self.__journal.pop(i)

    def get_balance(self) -> float:
        return sum(x.amount for x in self.__journal)
    
    def print_budget(self) -> None:
        for i, jr in enumerate(self.__journal):
            print(f'{i+1:>2}: {jr}')


budget = Budget()
for k, v in {'atlyginimai': -5000, 'ofiso nuoma': -1200.57, 'krano nuoma': 2000, 'pardavimai': 7500}.items():
    budget.add_record(JournalRecord(k, v))

# 

while True:
    inp = input(
        'komanda: 1 - isspausdinti biudzeta (); 2 - nauja bidzeto eilute (pavadinimas, suma); 3 - istrinti eilute (eilutes nr.); 4 - baigti.\n'
        'pvz. "1", "2 nauja eilute,100", "3 2", "4"\n')
    match inp[0]:
        case '1':
            budget.print_budget()
            print(f'balansas: {budget.get_balance():.2f}')
        case '2':
            l = inp.split(',')
            v1 = l[0][2:len(l[0])]
            v2 = float(l[1].replace(' ', ''))
            budget.add_record(JournalRecord(v1, v2))
            print(f'prideta eilute <{v1}: {v2}>')
        case '3':
            n = int(inp[2:len(inp)]) - 1
            print(f'istrinta eilute <{budget.pop_record(n)}>')
        case '4':
            break
        case _:
            print('bloga komanda, iveskite is naujo.')
