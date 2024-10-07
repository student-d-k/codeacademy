
a = float(input("Įveskite skaičių a: "))
b = float(input("Įveskite skaičių b: "))

o = input("Įveskite operaciją (+, -, *, /, //, %, **): ")

match o:
    case "+":
            print(a + b)
    case "-":
            print(a - b)
    case "*":
            print(a * b)
    case "/":
            print(a / b)
    case "//":
            print(a // b)
    case "%":
            print(a % b)
    case "**":
            print(a ** b)
    case _:
        print("Nežinoma operacija")
