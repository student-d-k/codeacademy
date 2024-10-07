
import pickle

class Employee:
    def __init__(self, a, b):
        self.aa = a
        self.b = b
    def prn_a(self):
        print(self.aa)
    def prn_b(self):
        print(self.b)

# with open(r"Fruits.obj", "wb") as output_file:
#     pickle.dump(Employee(2, 3),output_file)

# xx = Employee(4, 5)

with open(r"Fruits.obj", "rb") as input_file:
    x = pickle.load(input_file)

# x.prn_a()
x.prn_b()
