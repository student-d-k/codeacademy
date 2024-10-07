
import datetime as dt

class man:
    def __init__(self, _gender: str, _date_of_birth: str = '1900-01-01') -> None:
        self.gender = _gender
        self.date_of_birth = dt.datetime.strptime(_date_of_birth, '%Y-%m-%d')

    def age(self) -> dt.datetime:
        return dt.datetime.now() - self.date_of_birth
    
jonas = man('vyras', '2001-01-04')
petras = man('vyras')

print(jonas.age())

print(petras.age())
